import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
# iframe , frameset ,frame



# driver.get("https://the-internet.herokuapp.com/frames")
# driver.find_element(By.CSS_SELECTOR,"a[href='/iframe']").click()

# frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("I am able to automate")

driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)


time.sleep(2)