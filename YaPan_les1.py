import requests
import json
from pprint import pprint

username = 'YanaPan'
url = f'https://api.github.com/users/{username}/repos'

response = requests.get(url)
j_data = response.json()
# pprint(type(response.text))
# response.content
# response.text

pprint(type(j_data))

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)
