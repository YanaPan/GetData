import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.kinopoisk.ru'
params = {'quick_filters': 'serials',
          'tab': 'all',
          'page': 1}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

response = requests.get(url+'/popular/films', params=params, headers=headers)

dom = BeautifulSoup(response.text, 'html.parser')

serials_list = dom.find_all('div', {'class': 'desktop-rating-selection-film-item'})

serials = []


for serial in serials_list:
    serial_data = {}

    info = serial.find('p')
    name = info.getText()
    link = url + info.parent.get('href')

    genre = serial.find('span', {'class': 'selection-film-item-meta__meta-additional-item'}).next_sibling.getText()
    rating = serial.find('span', {'class': 'rating__value'}).getText()
    try:
        rating = float(rating)
    except:
        rating = None

    serial_data['name'] = name
    serial_data['link'] = link
    serial_data['genre'] = genre
    serial_data['rating'] = rating

    serials.append(serial_data)

pprint(serials)