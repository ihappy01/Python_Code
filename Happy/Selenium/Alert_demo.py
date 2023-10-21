import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")
driver.maximize_window()

# Failing
# ---------------------------------------------------
# Scroll till the element are visible
button=driver.find_element(By.XPATH,"//h2[@id='confirm']/following-sibling::p[1]/a")
driver.execute_script("arguments[0].click()",button)
# wait = WebDriverWait(driver,5)
# button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//h2[@id='confirm']/following-sibling::p[1]/a")))
# button.click()
# button = driver.find_element(By.XPATH,"//h2[@id='confirm']/following-sibling::p[1]/a")
# ActionChains(driver).scroll_to_element(button).perform()
# button.click()
# driver.find_element(By.XPATH,"//h2[@id='confirm']/following-sibling::p[1]/a").click()
time.sleep(5)

# -----------------------------------------------

#Working

# driver.find_element(By.LINK_TEXT,"See an example alert").click()
# alert = driver.switch_to.alert
# print(alert.text)
# # alert.accept()
# alert.dismiss()
# time.sleep(5)

