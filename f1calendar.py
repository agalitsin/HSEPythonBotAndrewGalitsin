
import requests
from bs4 import BeautifulSoup
import re

def upcomingraces():

    upcoming_races = []

    link = "https://ru.wikipedia.org/wiki/Формула-1_в_сезоне_2020" #ссылка на статью о сезоне ф1 2020
    website_url = requests.get(link).text #получаем код html
    soup = BeautifulSoup(website_url, 'lxml') #красиво размечаем html
    tables = soup.find_all('table') #сгружаем все таблички (нам нужны таблицы 6 и 7, то есть 5 и 6 по питонафске :) ) 
    rows = tables[5].find_all('tr') #нашли теперь все ряды в таблиц

    races = []
    racesdates = []
    
    for row in rows[1:]: #пробегаемся по табличке
        races.append(row.find_all('td')[0].text.strip().replace('[32]', '')) #добавляем название гран при в один список (убираем ненужные пометки )
        racesdates.append(row.find_all('td')[3].text.strip().replace('\xa0— ', '—')) #даты в другой список (убираем артефакты со стыка месяца)
        if row.find_all('td')[0].text.strip() == 'Гран-при Абу-Даби':
            break

    for n in range(len(races)):
        ourappend = [races[n], racesdates[n]]
        upcoming_races.append(ourappend)

    upcoming_races_text = ''   
    for n in upcoming_races:
        upcoming_races_text = upcoming_races_text + n[0] + ' \n' + n[1] + ' \n\n'

    upcomingraces = upcoming_races_text

    return upcomingraces

def deferredraces():

    deferred_races = []

    link = "https://ru.wikipedia.org/wiki/Формула-1_в_сезоне_2020" #ссылка на статью о сезоне ф1 2020
    website_url = requests.get(link).text #получаем код html
    soup = BeautifulSoup(website_url, 'lxml') #красиво размечаем html
    tables = soup.find_all('table') #сгружаем все таблички (нам нужны таблицы 6 и 7, то есть 5 и 6 по питонафске :) ) 

    rows = tables[6].find_all('tr')

    for row in rows[2:9]: #пробегаемся по табличке
        deferred_races.append(row.find_all('td')[0].text.strip())

    deferred_races_text = ''
    for n in deferred_races:
        deferred_races_text = deferred_races_text + n + ' \n'

    deferredraces = deferred_races_text

    return deferredraces

def canceledraces():
    
    deferred_races = []

    link = "https://ru.wikipedia.org/wiki/Формула-1_в_сезоне_2020" #ссылка на статью о сезоне ф1 2020
    website_url = requests.get(link).text #получаем код html
    soup = BeautifulSoup(website_url, 'lxml') #красиво размечаем html
    tables = soup.find_all('table') #сгружаем все таблички (нам нужны таблицы 6 и 7, то есть 5 и 6 по питонафске :) ) 

    rows = tables[6].find_all('tr')

    canceled_races = []
    canceled_races_dates = []

    for row in rows[10:13]: #пробегаемся по табличке
        canceled_races.append(row.find_all('td')[0].text.strip())
        canceled_races_dates.append(row.find_all('td')[3].text.strip())
    for n in range(len(canceled_races)):
        ourappend = [canceled_races[n], canceled_races_dates[n]]
        canceled_races[n] = ourappend

    canceled_races_text = ''   
    for n in canceled_races:
        canceled_races_text = canceled_races_text + n[0] + ' \n' + n[1] + ' \n\n'
    
    canceledraces = canceled_races_text

    return canceledraces
