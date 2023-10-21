# To find all the links in a web page
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()

# response = requests.head('https://tutorialsninja.com/demo/')
# print(response.status_code)

links = driver.find_elements(By.TAG_NAME,"a")

print(len(links))
# l=[]

for link in links:
    # l.append(link.text)
    url = link.get_attribute('href')
    res = requests.head(url)

