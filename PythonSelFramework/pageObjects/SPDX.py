from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set up webdriver
driver = webdriver.Chrome()  # replace with the path to your webdriver if needed
driver.get("https://dev.veedna.com/auth/signin")

# locate email and password fields and fill them in
email_field = driver.find_element_by_name("email")
password_field = driver.find_element_by_name("password")
email_field.send_keys("namurenobe-9946@yopmail.com")
password_field.send_keys("pwd.01234444444")
password_field.send_keys(Keys.RETURN)

# close the browser
driver.close()