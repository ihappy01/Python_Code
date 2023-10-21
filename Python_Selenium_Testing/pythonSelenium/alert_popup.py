import time

from selenium import webdriver
from selenium.webdriver.common.by import By

validate_text="Option3"
driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(validate_text)

driver.find_element(By.XPATH,"//input[@value='Alert']").click()
alert= driver.switch_to.alert
popup_text=alert.text
assert validate_text in popup_text
alert.accept() # To click on "Ok" button of popup

driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
confirm_popup= driver.switch_to.alert
confirm_popup.dismiss()
time.sleep(2) # To click on "cancel" or negative option button of popup