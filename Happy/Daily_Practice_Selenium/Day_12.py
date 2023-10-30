# wait
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://omayo.blogspot.com/')
driver.maximize_window()

# Implicit wait
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//*[text()='Dropdown']").click()
# driver.find_element(By.LINK_TEXT,'Flipkart').click()


#Explicit wait
# wait = WebDriverWait(driver,5)
#
# driver.find_element(By.XPATH,"//*[text()='Dropdown']").click()
# gmail_button = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Gmail')))
# gmail_button.click()


# Click using Java Script Executor
# dropdown_button = driver.find_element(By.XPATH,"//*[text()='Dropdown']")
# driver.execute_script('arguments[0].click()',dropdown_button)
# driver.implicitly_wait(5)
# driver.find_element(By.LINK_TEXT,'Flipkart').click()


#Click using ActionChains
action = ActionChains(driver)
dropdown_button = driver.find_element(By.XPATH,"//*[text()='Dropdown']")
action.click(dropdown_button).perform()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,'Flipkart').click()

time.sleep(5)