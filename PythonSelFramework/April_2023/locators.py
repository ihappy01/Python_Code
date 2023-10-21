import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,'email').send_keys("indrajeet@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Password@1234")
driver.find_element(By.ID,"exampleCheck1").click()


#Xpath- //tagname[@attribute='value']
#CSS-     tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Indrajeet")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success!" in message

time.sleep(9)



