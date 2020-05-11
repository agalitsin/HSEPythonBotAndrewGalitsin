
import pandas as pd
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np
import os

def forex_chart(forex, time): #0 - USDRUB; 1 - EURRUB; 0 - месяц; 1 - год

    nowtime = datetime.datetime.now() #получаем текущее время в формате 2020-04-10 12:49:41.222512

    if time == 0:
        fromtime = nowtime - timedelta(days=30) #получаем время месяц назад
    elif time == 1:
        fromtime = nowtime - timedelta(days=365) #получаем время год назад

    oururl = 'http://export.finam.ru/export9.out?market=5&em=' #прописываем начало ссылки которое одинаково для всех ссылок

    if forex == 0: #добавляем универсальные знаения цифрового и буквенного кода валютной пары
        em = '901'
        code = 'USDRUB'
    elif forex == 1:
        em = '66860'
        code = 'EURRUB'
        
    oururl = oururl + em + '&code=' + code + '&apply=0' #добавляем все необходимое к нашей ссылке (что собирали выше)

    oururl = oururl + '&df=' + str(fromtime.day) + '&mf=' + str(int(fromtime.month) - 1) + '&yf=' + str(fromtime.year) #добавили начальные числа дат (месяца по ссылке считаются с 0 до 11)

    oururl = oururl + '&from=' + fromtime.strftime("%d.%m.%Y") #доабвили тег from

    oururl = oururl + '&dt=' + str(nowtime.day) + '&mt=' + str(int(nowtime.month) - 1) + '&yt=' + str(nowtime.year)

    oururl = oururl + '&to=' + nowtime.strftime("%d.%m.%Y") #доабвили тег to

    if time == 0:
        p = '8'
    elif time == 1:
        p = '9'
        
    oururl = oururl + '&p=' + p #добавили временной период для каждой строки (8 - день, 9 - год)

    oururl = oururl + '&f=' + code + '_' + fromtime.strftime("%d%m%Y") + '_' + nowtime.strftime("%d%m%Y") #добавили тег для имени файла

    oururl = oururl + '&e=.csv' + '&cn=' + code #добавили расширение файла и название первой колонки

    oururl = oururl + '&dtf=4&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=3&sep2=1&datf=2&at=1' #добавили форматы даты и времени и остальыне данные, которые у всех ссылок одинаковые

    #получили нашу крутую мэджик-ссылку

    df = pd.read_csv(oururl, delimiter=';')
    df.columns = df.columns.str.replace('<', '')
    df.columns = df.columns.str.replace('>', '')

    if time == 0: #создаем название
        grafname = 'Граффик ' + code + ' за прошедший месяц:'
    elif time == 1:
        grafname = 'Граффик ' + code + ' за прошедший год:'

    df.plot(x='DATE', y='CLOSE') # создаем график
    plt.legend().set_visible(False)
    plt.title(grafname)
    plt.grid()

    plt.savefig('plt.png') #сохраняем график