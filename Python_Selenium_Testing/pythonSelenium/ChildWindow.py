import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()

childwindow = driver.window_handles[1]
print("The child window id is ",childwindow)

driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text


time.sleep(2)