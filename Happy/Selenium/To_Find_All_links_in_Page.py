from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,"a")

print(len(links))