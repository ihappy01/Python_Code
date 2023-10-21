from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/?locale=in")


driver.find_element(By.CSS_SELECTOR,"#username").send_keys("Indrajeet")

driver.find_element(By.CSS_SELECTOR,".password").send_keys("Happy@123")
driver.find_element(By.CSS_SELECTOR,".password").clear()

driver.find_element(By.LINK_TEXT,"Forgot Your Password?").click()

#  below xpath using text is not working
# driver.find_element(By.XPATH,"//a[text()='Cancel").click()
driver.find_element(By.CSS_SELECTOR,".secondary").click()



print(driver.find_element(By.XPATH,"//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR,".label[for='password']").text)
print(driver.find_element(By.CSS_SELECTOR,"form[name='login'] label:nth-child(2)").text)
# //div[@id='usernamegroup']/label
# div[id='usernamegroup'] label