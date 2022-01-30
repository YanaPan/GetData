import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'http://127.0.0.1:5000/'

response = requests.get(url)

dom = BeautifulSoup(response.text, 'html.parser')

tag_a = dom.find('a')
# pprint(tag_a)
# print(type(tag_a))

parent_a = tag_a.parent.parent
# pprint(parent_a)

# for tag in parent_a:
#     print(tag)

result = list(parent_a.children)
# pprint(result)

result2 = list(parent_a.findChildren(recursive=False))
# pprint(result2)

div_d = dom.find('p', {'id': 'd2'})
# print(div_d)

p_special = dom.find_all('p', {'class': 'paragraph', 'id': 'clickable'})
# pprint(p_special)

p_tags = dom.find_all('p', {'class': 'paragraph'})
# pprint(p_tags)

p_tags = dom.find_all('p', {'class': ['red', 'paragraph']})
# pprint(p_tags)

p_tags = dom.select('p.paragraph.red')
# pprint(p_tags)

p6 = dom.find(text='РЁРµСЃС‚РѕР№ РїР°СЂР°РіСЂР°С„')
# pprint(p6.parent)

body = dom.find('body')
p6p7 = body.find_all('p', recursive=False)
pprint(p6p7)

