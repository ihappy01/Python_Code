# Implicit wait
# Explicit wait
# Pause the test for few seconds using Time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ber")
time.sleep(2)

print(len(driver.find_elements(By.CSS_SELECTOR,"div.products div.product")))

buttons= driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4

selected_veg=[]

for button in buttons:
    selected_veg.append(button.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    button.click()

print(selected_veg)
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()


wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))

veg_after_selection=[]
veggies= driver.find_elements(By.CSS_SELECTOR,"p.product-name")

for veg in veggies:
    veg_after_selection.append(veg.text)

print(veg_after_selection)
assert selected_veg == veg_after_selection

original_amount= driver.find_element(By.CSS_SELECTOR,".discountAmt").text
print("Total amount before discount",original_amount)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()


wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

discount_amount= driver.find_element(By.CSS_SELECTOR,".discountAmt").text
print("Total amount after discount",discount_amount)
assert int(original_amount) > float(discount_amount)

amounts= driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0

for amoumt in amounts:
    sum = sum + int(amoumt.text)

print("Total Amount is ",sum)

total_amount_displayed =int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == total_amount_displayed




time.sleep(2)
