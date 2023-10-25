import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
base_window_ID = driver.current_window_handle
print(base_window_ID)

driver.find_element(By.LINK_TEXT,"Click Here").click()


driver.switch_to.window(base_window_ID)
driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()
time.sleep(5)

windows = driver.window_handles
print(windows)

for w in windows:
    driver.switch_to.window(w)
    if driver.title.__eq__("Elemental Selenium | Elemental Selenium"):
        para_one_text=driver.find_element(By.XPATH,"//h1").text
        print(para_one_text)
    elif driver.title.__eq__("The Internet"):
        text= driver.find_element(By.XPATH,"//h3").text
        print(text)
