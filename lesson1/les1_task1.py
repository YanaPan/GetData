import requests
import json
from pprint import pprint

username = 'YanaPan'
url = f'https://api.github.com/users/{username}/repos'

response = requests.get(url)
j_data = response.json()
j_dir = [{'name': j.get('name'), 'url': j.get('html_url')} for j in j_data]

pprint(j_dir)

with open('task1.json', 'w') as file:
    json.dump(j_dir, file)
