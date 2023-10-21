from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver
    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # driver.find_element(By.XPATH, "//button[contains(@class,'btn-success')]").click()
    products = (By.XPATH, "//div[@class='card h-100']")

    def getProductNames(self):
        return self.driver.find_elements(*CheckoutPage.products)
