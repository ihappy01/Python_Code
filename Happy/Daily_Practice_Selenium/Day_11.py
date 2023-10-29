# # Right click practice
# import time
#
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import requests

# driver = webdriver.Chrome()
# driver.get('https://tutorialsninja.com/demo/')
# driver.maximize_window()
#
#
# action = ActionChains(driver)
#
# text_field = driver.find_element(By.NAME,'search')
#
# action.context_click(text_field).context_click()
#
# time.sleep(5)
#
# # ----------------------------------

# To find all the links on the page

driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/tvs-appliances-the-big-diwali-sale-store?fm=neo%2Fmerchandising&iid=M_585a9161-bfa5-4491-9119-f4f0ce5eb60e_1_FBB4FBSRQIC6_MC.KCBBC8GGWR9V&otracker=hp_rich_navigation_4_1.navigationCard.RICH_NAVIGATION_TVs%2B%2526%2BAppliances_KCBBC8GGWR9V&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L0_view-all&cid=KCBBC8GGWR9V')
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,'a')
print("Total number of links on the page:",len(links))

urls=[]
for link in links:
    url=link.get_attribute('href')
    urls.append(url)

    response = requests.head(url)

    if response.status_code !=200:
        print(f"{url} is broken and {response.status_code} is response code")

else:
    print("All Links are woring")

print(urls)







