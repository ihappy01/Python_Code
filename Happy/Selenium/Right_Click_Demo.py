import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

action = ActionChains(driver)

search_box =driver.find_element(By.XPATH,"//div[@id='search']/input")
# action.context_click(search_box).perform()
action.double_click(search_box).perform()

time.sleep(5
           )