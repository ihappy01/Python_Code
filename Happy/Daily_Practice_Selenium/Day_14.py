import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')

parent_window=driver.current_window_handle

driver.find_element(By.LINK_TEXT,'Click Here').click()

windows = driver.window_handles

for window in windows:
    if window!= parent_window:
        driver.switch_to.window(window)
        print(driver.find_element(By.TAG_NAME,'h3').text)
        # driver.quit()

driver.switch_to.window(parent_window)
print(driver.find_element(By.TAG_NAME,'h3').text)
time.sleep(5)