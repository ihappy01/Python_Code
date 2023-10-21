# Implicit wait
# Explicit wait
# Pause the test for few seconds using Time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# wait until 5 sec if object is not displayed
# Global Wait
# 1.5 sec to reach text page - execution will resume in 1.5 sec
# if object do not show up at all, then max time your test waits for 5 sec
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ber")
time.sleep(2)

print(len(driver.find_elements(By.CSS_SELECTOR,"div.products div.product")))

buttons= driver.find_elements(By.XPATH,"//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
time.sleep(2)