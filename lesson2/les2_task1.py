import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

search = input('Введите наименование вакансии: ')

url = 'https://hh.ru/search/vacancy'
params = {'area': 1,
          'fromSearchLine': 'true',
          'text': search,
          'from': 'suggest_post',
          'page': '0',
          'hhtmFrom': 'vacancy_search_list'
          }

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
response = requests.get(url, params=params, headers=headers)
dom = BeautifulSoup(response.text, 'html.parser')
vacancy_list = dom.find_all('div', {'class': 'vacancy-serp-item__row_header'})

vacancies = []
page_num = 0
while vacancy_list:
    for vacancy in vacancy_list:
        vacancy_data = {}

        info = vacancy.find('a')
        vacancy_data['name'] = info.getText()
        vacancy_data['link'] = info.get('href')

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

        vacancy_data['source'] = 'hh.ru'
        vacancies.append(vacancy_data)

    page_num += 1
    params['page'] = str(page_num)
    dom = BeautifulSoup(requests.get(url, params=params, headers=headers).text, 'html.parser')
    vacancy_list = dom.find_all('div', {'class': 'vacancy-serp-item__row_header'})

pprint(vacancies)

with open('lesson2.json', 'w') as file:
    json.dump(vacancies, file)

