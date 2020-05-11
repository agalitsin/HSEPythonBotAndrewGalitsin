#создаем словари валют
#певый - пара код валюты-курс
#второй - русское наименование валюты, в значении список из кода валюты и  кода эмодзи флага страны ТГ

import xml.etree.ElementTree as ET
from collections import OrderedDict
from copy import copy
import requests

def dictify(r,root=True): #это взял из инета - функция позволяет сделать из xml список словарей
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["_text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

def courses(coursename):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp') #достает наш json и делаем из него список словарей
    r = ET.fromstring(r.text)
    
    d = dictify(r)

    coursedict = d['ValCurs']['Valute'] #убираем главный ключь (данные о валютах лежат в нем как в подпапке)
    corsesnames = {} #словарб из наименования валюты и его кода, позже добавим проме кода и код его эмоджы в телеграм, чтобы на кнопке в python отображался флаг
    ourbeasts = ['AUD', 'SGD', 'CNY', 'CAD', 'KZT', 'EUR', 'USD', 'BYN', 'GBP'] #тут пишем коды валют которые хотим вытащить

    for n in coursedict: #проходимся по словарю с курсами
        for nn in ourbeasts: #сравниваем их код с тем что нам нужно
            if n['CharCode'][0]['_text'] == nn: 
                corsesnames[n['Name'][0]['_text']] = n['Value'][0]['_text']

    corsesnames['Фунт стерлингов'] = corsesnames['Фунт стерлингов Соединенного королевства']
    del corsesnames['Фунт стерлингов Соединенного королевства']      

    return(corsesnames[coursename])