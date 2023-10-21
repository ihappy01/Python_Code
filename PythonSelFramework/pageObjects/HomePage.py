from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"[href*='shop']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
        # driver.find_element(By.CSS_SELECTOR, "[href*='shop']").click()
