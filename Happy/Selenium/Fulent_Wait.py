import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()


driver.find_element(By.CSS_SELECTOR,'button.dropbtn').click()
driver.find_element(By.LINK_TEXT,'Facebook').click()