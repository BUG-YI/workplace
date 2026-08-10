from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com'

driver = webdriver.Edge()
print(12)
driver.get(url)
# input()

source = driver.page_source
print(source)
element = driver.find_element(By.ID, '')
driver.execute_script('sleep(1)')

driver.close()