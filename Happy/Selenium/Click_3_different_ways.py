import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()


button=driver.find_element(By.ID,"alert1")

#Using Action
# action = ActionChains(driver)
# action.click(button).perform()

#Using Normal click
# button.click()

#Using JavaScript Executor
driver.execute_script("arguments[0].click()",button)

time.sleep(3)