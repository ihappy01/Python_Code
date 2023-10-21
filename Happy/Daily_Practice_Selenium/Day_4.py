import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID,'alert1').click()
time.sleep(5)

# wait = WebDriverWait(driver,5)
# alert = wait.until(expected_conditions.alert_is_present())
#
# print(alert.text)
# alert.accept()

alert = driver.switch_to.alert
print(alert.text)
# alert.accept()
alert.dismiss()
driver.find_element(By.ID,'ta1').send_keys("Indrajeet")
time.sleep(5)