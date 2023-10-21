from asyncio import wait
from datetime import time

from selenium import webdriver

# Browser exposes an executable file
# Through selenium test we need to invoke the executable file which will then invoke
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver.get("https://www.google.com/")
# driver.get("https://rahulshettyacademy.com/")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.back()

driver.refresh()


