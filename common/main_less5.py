from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://gb.ru/login')

elem = driver.find_element(By.ID, 'user_email')
elem.send_keys('study.ai_172@mail.ru')

elem = driver.find_element(By.ID, 'user_password')
elem.send_keys('Password172')

elem.send_keys(Keys.ENTER)
# ---------
elem = driver.find_element(By.XPATH, "//a[contains(@href,'/users/')]")
link = elem.get_attribute('href')
driver.get(link)

elem = driver.find_element(By.CLASS_NAME, "text-sm")
link = elem.get_attribute('href')
driver.get(link)

elem = driver.find_element(By.NAME, "user[time_zone]")
select = Select(elem)
select.select_by_value('Athens')

elem.submit()

driver.refresh()
driver.back()
driver.forward()

print()

# driver.quit()