import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

driver.find_element(By.ID,"hide-textboxi").click()

text_field = driver.find_element(By.ID,'displayed-text')
driver.execute_script("arguments[0].value='Indrajeet'",text_field)


time.sleep(5)