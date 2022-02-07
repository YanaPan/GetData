from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
from pymongo import errors
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)
db = client['goods070222']
mvideo = db.mvideo

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

driver.get('https://www.mvideo.ru/')
driver.implicitly_wait(10)

html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.PAGE_DOWN)

goods = driver.find_elements(By.XPATH,
                             "//h2[contains(text(), 'Хиты продаж')]/..//a[@class='img-with-badge ng-star-inserted']")
links = []
for good in goods:
    link = good.get_attribute('href')
    links.append(link)

for link in links:
    dic = {}
    dic['_id'] = int(str(link)[-8:])
    dic['link'] = link
    driver.get(link)
    dic['name'] = driver.find_element(By.TAG_NAME, 'h1').text
    dic['price'] = driver.find_element(By.CLASS_NAME, 'price__main-value').text.replace("&nbsp", " ")
    driver.back()
    try:
        mvideo.insert_one(dic)
    except errors:
        print(errors)

for doc in mvideo.find({}):
    pprint(doc)
