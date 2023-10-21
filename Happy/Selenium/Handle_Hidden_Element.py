import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Raise selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable( as element is hidden)
# driver.find_element(By.ID,"hide-textbox").click()
# driver.find_element(By.ID,"displayed-text").send_keys("Indrajeet")

driver.find_element(By.ID,"hide-textbox").click()
# To enter in the hidden text_field
text_field = driver.find_element(By.ID,"displayed-text")
driver.execute_script("arguments[0].value='Indrajeet'",text_field)

time.sleep(5)
