import time

from selenium import webdriver

def test_one():
    driver = webdriver.Chrome()
    driver.get("http://omayo.blogspot.com/")
    time.sleep(5)
    driver.quit()

def test_tutorial_ninja():
    driver = webdriver.Chrome()
    driver.get('https://tutorialsninja.com/demo/')
    time.sleep(5)
    driver.quit()

def test_selenium_143():
    driver = webdriver.Chrome()
    driver.get('https://selenium143.blogspot.com/')
    time.sleep(5)
    driver.quit()

def test_selenium_by_arun():
    driver = webdriver.Chrome()
    driver.get('https://selenium-by-arun.blogspot.com/')
    time.sleep(5)
    driver.quit()

def test_compendium_dev():
    driver = webdriver.Chrome()
    driver.get('https://testpages.eviltester.com/styled/basic-web-page-test.html')
    time.sleep(5)
    driver.quit()



def test_jquery():
    driver = webdriver.Chrome()
    driver.get('https://jqueryui.com/')
    time.sleep(5)
    driver.quit()