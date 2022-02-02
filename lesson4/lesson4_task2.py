import pymongo
from pymongo import MongoClient
from pymongo import errors
from pprint import pprint
from lxml import html
import requests

client = MongoClient('127.0.0.1', 27017)
db = client['news020222']
lenta = db.lenta

url = 'https://lenta.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

response = requests.get(url, headers=headers)

dom = html.fromstring(response.text)
links = dom.xpath("//div/a[contains(@class,'_topnews')]/@href")

for link in links:
    response2 = requests.get(url + link, headers=headers)
    dom2 = html.fromstring(response2.text)
    news = {}
    name = dom2.xpath(".//h1/span/text()")
    time = dom2.xpath(".//time[contains(@class, 'topic-header__time')]/text()")

    news['name'] = name[0]
    news['link'] = url + link
    news['time'] = time[0]
    news['source'] = 'lenta.ru'

    try:
        lenta.insert_one(news)
    except errors:
        print(errors)

for doc in lenta.find({}):
    pprint(doc)
