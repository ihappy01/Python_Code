from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.implicitly_wait(10)

# driver.find_element(By.NAME,"name").send_keys("Indrajeet")
# driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Indrajeet")
driver.find_element(By.CSS_SELECTOR, "input[minlength='2']").send_keys("Indrajeet")

driver.find_element(By.NAME, "email").send_keys("ihappy@gmail.com")

driver.find_element(By.ID, "exampleCheck1").click()

#Handling Static Dropdown
# select class provide the methods to handle the options in the dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


# driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# print(driver.find_element(By.CLASS_NAME, "alert-success").text)
# print(driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text)
print(driver.find_element(By.XPATH,"//*[contains(@class,'alert-success')]").text)
message = driver.find_element(By.XPATH,"//*[contains(@class,'alert-success')]").text

assert "success!" in message

# print(driver.title)
# print(driver.current_url)
