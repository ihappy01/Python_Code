# We can switch to frame
# using ID or name
# using Webelement
# using Index
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/iframe')
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH,"//body[@id='tinymce']").clear()
driver.find_element(By.XPATH,"//body[@id='tinymce']").send_keys("Indrajeet")
time.sleep(5)