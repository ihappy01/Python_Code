import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://omayo.blogspot.com/')
print(driver.title)
driver.maximize_window()


# driver.implicitly_wait(5)
#
# driver.find_element(By.CLASS_NAME,'dropbtn').click()
# driver.find_element(By.LINK_TEXT,'Facebook').click()
#
# time.sleep(3)

wait = WebDriverWait(driver,5)#

driver.find_element(By.CLASS_NAME,'dropbtn').click()

facebook_button = wait.until(expected_conditions.visibility_of_element_located(((By.LINK_TEXT,'Facebook'))))
facebook_button.click()

time.sleep(3)
