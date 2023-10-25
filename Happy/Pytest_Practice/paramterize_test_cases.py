import pytest
from selenium import webdriver

@pytest.mark.parametrize('browser',["chrome","firefox",'edge'])
def test_cross_browser(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=='edge':
        driver=webdriver.Edge()

    driver.get("https://www.selenium.dev/")
    driver.close()

