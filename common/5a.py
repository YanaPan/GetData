from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("")

driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
driver.implicitly_wait(10)

driver.get('https://5ka.ru/rating/catalogue')

elem = driver.find_element(By.XPATH, "//span[contains(text(), 'РџСЂРёРЅСЏС‚СЊ')]/../..")
elem.click()

pages = 0
while pages < 5:
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'add-more-btn')))

    button.click()
    pages += 1

goods = driver.find_elements(By.CLASS_NAME, 'product-card')
for good in goods:
    short_name = good.find_element(By.CLASS_NAME, 'item-name')
    short_name.click()
    aside = driver.find_element(By.TAG_NAME, 'aside')
    name = aside.find_element(By.XPATH, "//h2").text
    good.send_keys(Keys.ESCAPE)

    print(name)
