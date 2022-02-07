import pymongo
from pymongo import MongoClient
from pymongo import errors
import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)
db = client['vacancies']
hh = db.hh

search = input('Введите наименование вакансии: ')

url = 'https://hh.ru/search/vacancy'
params = {'text': search,
          'page': '0'}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
response = requests.get(url, params=params, headers=headers)
dom = BeautifulSoup(response.text, 'html.parser')
vacancy_list = dom.find_all('div', {'class': 'vacancy-serp-item__row_header'})

page_num = 0
while vacancy_list:
    for vacancy in vacancy_list:
        vacancy_data = {}

        info = vacancy.find('a')
        vacancy_data['name'] = info.getText()
        link = info.get('href')
        vacancy_data['_id'] = int(re.findall(r'vacancy/(.+?)from', str(link).replace('?', ''))[0])
        vacancy_data['link'] = link
        vacancy_data['source'] = 'hh.ru'

        try:
            salary = vacancy.find('div', {'class': 'vacancy-serp-item__sidebar'}).getText()
            salary = salary.replace('\u202f', '').replace('\xa0', '')
            salary_detail = salary.split()
            vacancy_data['currency'] = salary_detail[-1]
            if salary_detail[0] == 'от':
                vacancy_data['salary_min'] = int(salary_detail[1])
                vacancy_data['salary_max'] = None
            elif salary_detail[0] == 'до':
                vacancy_data['salary_min'] = None
                vacancy_data['salary_max'] = int(salary_detail[1])
            else:
                vacancy_data['salary_min'] = int(salary_detail[0])
                vacancy_data['salary_max'] = int(salary_detail[2])
        except:
            vacancy_data['currency'] = None
            vacancy_data['salary_min'] = None
            vacancy_data['salary_max'] = None

        try:
            hh.insert_one(vacancy_data)
        except errors.DuplicateKeyError:
            print(f'Вакансия {vacancy_data["_id"]} уже есть в базе данных')  # добавление только новых вакансий

    page_num += 1
    params['page'] = str(page_num)
    dom = BeautifulSoup(requests.get(url, params=params, headers=headers).text, 'html.parser')
    vacancy_list = dom.find_all('div', {'class': 'vacancy-serp-item__row_header'})

for vacancy in hh.find({'$or': [{'salary_min': {'$gt': 100000}}, {'salary_max': {'$gt': 100000}}]}):
    pprint(vacancy) # ввыведение информации по вакансиям с зарплатой от 100 000

# for vacancy in hh.find({}):
#     pprint(vacancy)
