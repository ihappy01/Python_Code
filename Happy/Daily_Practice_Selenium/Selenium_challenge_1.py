from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver.get('https://www.worldometers.info/world-population/')
driver.maximize_window()


current_world_population= driver.find_element(By.XPATH,"//div[@class='maincounter-number']").text
print("The current world population is : ",current_world_population)