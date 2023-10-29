import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://omayo.blogspot.com/')
driver.maximize_window()

driver.find_element(By.ID,'alert1').send_keys(Keys.ENTER)

time.sleep(5)