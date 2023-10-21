import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"[href*='shop']").click()

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

# //div[@class='card h-100/div/h4/a
# product = //div[@class='card h-100

for product in products:
    productName =product.find_element( By.XPATH,"div/h4/a").text
    if productName =="Blackberry":
        #Add item in the cart
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"[class*='btn-primary']").click()

#  //button[@class='btn btn-success']
#  //button[contains(@class,'btn-success')]
driver.find_element(By.XPATH,"//button[contains(@class,'btn-success')]").click()


driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")

wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
print(driver.find_element(By.CLASS_NAME,"alert-success").text)
message = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in message

driver.get_screenshot_as_file("screen.png")

time.sleep(2)