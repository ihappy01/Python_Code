import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("http://omayo.blogspot.com/")
# driver.maximize_window()

# driver.implicitly_wait(5)

# wait = WebDriverWait(driver,5)
#
# driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()
#
# # facebook_button = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Gmail")))
# # facebook_button = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,"Gmail")))
# facebook_button = wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Gmail")))
# # driver.find_element(By.LINK_TEXT,"Gmail").click()
# facebook_button.click()

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='Login']").click()
print(driver.find_element(By.XPATH,"//div[contains(@class,'alert')]").text)
time.sleep(5)