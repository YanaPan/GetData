from pprint import pprint
from lxml import html
import requests

url = 'https://ru.ebay.com/b/Fishing-Equipment-Supplies/1492/bn_1851047'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

response = requests.get(url, headers=headers)

dom = html.fromstring(response.text)
items = dom.xpath("//li[contains(@class,'s-item')]")
fishing = []
for item in items:
    fish = {}
    name = item.xpath(".//h3[@class='s-item__title']/text()")
    link = item.xpath(".//h3[@class='s-item__title']/../@href")
    price = item.xpath(".//span[@class='s-item__price']//text()")
    add_info = item.xpath(".//span[contains(@class,'s-item__hotness')]/span/text()")

    fish['name'] = name[0]
    fish['price'] = price
    fish['add_info'] = add_info
    fish['link'] = link[0]

    fishing.append(fish)

pprint(fishing)