import time
from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getProductNames()

        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        # //div[@class='card h-100/div/h4/a
        # product = //div[@class='card h-100

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                # Add item in the cart
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-primary']").click()

        #  //button[@class='btn btn-success']
        #  //button[contains(@class,'btn-success')]
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-success')]").click()

        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")

        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        print(self.driver.find_element(By.CLASS_NAME, "alert-success").text)
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in message

        self.driver.get_screenshot_as_file("screen.png")

        time.sleep(2)
