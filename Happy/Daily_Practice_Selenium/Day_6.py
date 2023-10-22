import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://omayo.blogspot.com/')
driver.maximize_window()

# id="drop1"
dropdown_button = driver.find_element(By.ID,"drop1")
select = Select(dropdown_button)

# select.select_by_value('ghi')
# time.sleep(4)


select.select_by_index(4)
time.sleep(5)
