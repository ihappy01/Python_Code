from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://omayo.blogspot.com/')

row= driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
print(len(row))

col= driver.find_elements(By.XPATH,"//table[@id='table1']//th")
print(len(col))



''''To fetch value from table '''

print(driver.find_element(By.XPATH,"//table[@id='table1']//tr[2]//td[3]").text)