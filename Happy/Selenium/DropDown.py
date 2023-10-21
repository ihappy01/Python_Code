import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://omayo.blogspot.com/')

dropdown_field = driver.find_element(By.ID,"drop1")

select=Select(dropdown_field)
select.select_by_visible_text('doc 3')
# select.select_by_index(1)
# select.select_by_value("mno")


# if select.is_multiple:
#     print("Multiple-selection box field")
# else:
#     print("Dropdown field")
# time.sleep(3)


# drop_down_options = select.options
#
# for option in drop_down_options:
#     print(option.text)


# print(select.first_selected_option.text)

