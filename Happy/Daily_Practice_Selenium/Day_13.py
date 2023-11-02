import time

from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
# #
#
# # Explict Wait
# # driver.find_element(By.XPATH,"//*[text()='Dropdown']").click()
# #
# # wait = WebDriverWait(driver,7)
# #
# # facebook_btn = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Flipkart")))
# # facebook_btn.click()
# #



# Different types of click()

# Using ActionChains
# action = ActionChains(driver)
# btn = driver.find_element(By.ID,"alert1")
# action.click(btn).perform()

#Using Javascript Executor
# btn = driver.find_element(By.ID,"alert1")
# driver.execute_script('arguments[0].click()',btn)



# Right Click operation
# driver.get("https://tutorialsninja.com/demo/")
# driver.maximize_window()
#
# search_btn= driver.find_element(By.XPATH,"//input[@name='search']")
# action = ActionChains(driver)
# action.context_click(search_btn).perform()


# Dropdown
dropdown = driver.find_element(By.ID,'drop1')
select = Select(dropdown)
# select.select_by_visible_text('doc 1')
# select.select_by_value('ghi')
select.select_by_index(1)
time.sleep(5)
