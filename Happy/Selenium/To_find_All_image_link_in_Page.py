from selenium import webdriver


from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Selenium WebDriver (make sure you have installed the appropriate driver)
driver = webdriver.Chrome()

# URL of the webpage
url = "https://www.flipkart.com/two-wheelers-store?fm=neo%2Fmerchandising&iid=M_dca5ac0a-2f76-49b2-b450-128d90f31f6c_1_372UD5BXDFYS_MC.SCJPZ04TFJJM&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Two%2BWheelers~Petrol%2BVehicles_SCJPZ04TFJJM&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L1_view-all&cid=SCJPZ04TFJJM"

# Open the URL
driver.get(url)

# Find all img elements
img_elements = driver.find_elements(By.TAG_NAME,"img")

# Extract and print the alt attribute of each image (image name)
for img_element in img_elements:
    img_name = img_element.get_attribute("alt")
    if img_name:
        print(img_name)

# Close the WebDriver
driver.quit()
