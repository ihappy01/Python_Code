import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


#-------------------------Wait---------------------
# driver = webdriver.Chrome()
# driver.get("http://omayo.blogspot.com/")
# driver.maximize_window()
#
#
# driver.find_element(By.CLASS_NAME,"dropbtn").click()
#
# # driver.implicitly_wait(5)
# # driver.find_element(By.LINK_TEXT,"Facebook").click()
# # time.sleep(5)
#
# wait = WebDriverWait(driver,5)
#
# facebook_btn = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Facebook')))
# facebook_btn.click()
# time.sleep(5)

#----------------------------------------------------------------

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,'See an example alert').click()



alert = driver.switch_to.alert
# print(alert.text)
alert.accept()

driver.find_element(By.XPATH,"//div[contains(@class,'td-page-meta')]/a[1]").click()
time.sleep(5)
