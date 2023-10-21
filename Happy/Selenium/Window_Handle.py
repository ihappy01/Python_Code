import  time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()

parent_win = driver.current_window_handle
# print(parent_win)


driver.find_element(By.LINK_TEXT,"Click Here").click()
windows  = driver.window_handles

for window in windows:
    if .title.__eq__("New Window"):
        driver.switch_to(window)
        print(driver.find_elements(By.TAG_NAME,"h3").text)

        time.sleep(5)

time.sleep(5)


