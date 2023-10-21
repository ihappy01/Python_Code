import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# action = ActionChains(driver)
#
# menu = driver.find_element(By.CSS_SELECTOR,"#mousehover")
#
# action.move_to_element(menu).perform()
# childmenu = driver.find_element(By.LINK_TEXT," Reload")
#
# action.move_to_element(childmenu).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)

action.context_click(driver.find_element(By.CSS_SELECTOR,"#double-click")).perform()
action.double_click(driver.find_element(By.CSS_SELECTOR,"#double-click")).perform()
time.sleep(2)
alert = driver.switch_to.alert

print(alert.text)
alert.accept()




time.sleep(2)