import time
# from _ast import arguments

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/')
driver.maximize_window()

driver.implicitly_wait(5)


base_window = driver.current_window_handle
print(base_window)

button = driver.find_element(By.XPATH,"//img[@alt='Travel']")
driver.execute_script('arguments[0].click()',button)


windows = driver.window_handles
print(windows)


