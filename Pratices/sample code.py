from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# 1. Launch browser
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.geeksforgeeks.org/selenium-python-tutorial/")

# # 3. Find search box and type query
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Selenium Python")

# # 4. Wait and press Enter
# time.sleep(2)  # Wait for suggestions to load
# search_box.submit()  # Press Enter

# 5. Wait and take a screenshot
time.sleep(3)

driver.save_screenshot("search_results.png")


actions = ActionChains(driver)
actions.




# 6. Close browser
driver.quit()
