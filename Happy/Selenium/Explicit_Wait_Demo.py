import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()

# ----------------------
# wait = WebDriverWait(driver,timeout=4)
#
# driver.find_element(By.CSS_SELECTOR,'button.dropbtn').click()
# # driver.find_element(By.LINK_TEXT,'Facebook').click()
#
# facebook_button = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Facebook')))
# facebook_button.click()
#
# time.sleep(5)
# -------------------------

wait = WebDriverWait(driver,5)

# driver.find_element(By.ID,'timerButton')

timer_button = wait.until(expected_conditions.element_to_be_clickable((By.ID,'timerButton')))
timer_button.click()

time.sleep(5)