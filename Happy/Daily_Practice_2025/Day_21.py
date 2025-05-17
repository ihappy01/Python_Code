from selenium import webdriver


d =webdriver.Chrome()
d.get("https://www.flipkart.com/")

print(d.title)