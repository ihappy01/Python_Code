# JavascriptExecutor is a predefined interface in Selenium WebDriver API
# using execute_script we can run Javascript code in selenium
# we generally use JavascriptExecutor in selenium webdriver,
#   -When normal click() is not working
#   -Selenium webdriver don't have the capacity to scroll the page
#   -Add many more cases, where selenium webdriver's default things are not going to help (To Handle Hidden Element)


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()


# Scroll till the element are visible
# drop_down_button=driver.find_element(By.CLASS_NAME,"dropbtn")
# driver.execute_script("arguments[0].scrollIntoView(true)",drop_down_button)  #Javascript code

#Scroll by certain distance
# driver.execute_script("window.scrollBy(0,600)")
time.sleep(3)
#When normal click does not work than we use javascript Executor
button =driver.find_element(By.ID,"alert1")
# driver.find_element(By.ID,"alert1").click()

driver.execute_script("arguments[0].click()",button)
time.sleep(3)
