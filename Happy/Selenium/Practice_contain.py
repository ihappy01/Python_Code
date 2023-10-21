from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get('https://www.kent.qa.eschein.com/')
# print(driver.find_element(By.XPATH,"//h4[contains(text(),'Finance')]").text)

#To find single element and print it
# driver.get('https://www.selenium.dev/selenium/web/linked_image.html')
# print(driver.find_element(By.CSS_SELECTOR,"#justanotherLink").text)
#
# # To find multiple element and print the text
# texts=driver.find_elements(By.XPATH,"//a[contains(text(),'link')]")
# for ob in texts:
#     print(ob.text)


#Text function demo
driver.get("http://omayo.blogspot.com/")
driver.find_element(By.XPATH,"//button[text()='Submit']").click()