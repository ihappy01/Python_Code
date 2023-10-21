import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# check_boxes =driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
check_boxes =driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(check_boxes))

for checkbox in check_boxes:
    #
    if checkbox.get_attribute('value') =="option2":
        checkbox.click()
        assert checkbox.is_selected()
    # checkbox.click()
    # assert checkbox.is_selected()
    # print(checkbox.is_selected())

radiobuttons = driver.find_elements(By.CSS_SELECTOR,"input[name='radioButton']")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

time.sleep(2)
print("Hide tab is displayed or not ",driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_selected())

driver.find_element(By.CSS_SELECTOR,"#hide-textbox").click()
time.sleep(2)


print("Hide tab is displayed or not ",driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_selected())




# input[name='radioButton']
#  //input[@name='radioButton']