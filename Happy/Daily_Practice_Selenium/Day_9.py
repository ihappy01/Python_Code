import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://omayo.blogspot.com/')
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()

# fb_button=driver.find_element()

wait =WebDriverWait(driver,5)
fb_button=wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Facebook')))
fb_button.click()
time.sleep(5)

