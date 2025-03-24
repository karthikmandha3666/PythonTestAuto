import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")



driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("ind")
time.sleep(2)

text_field = driver.find_elements(By.CSS_SELECTOR, "li[class$='ui-menu-item'] div")
print(f"Found {len(text_field)} items")

for text_select in text_field:
    if text_select.text == "India":
        text_select.click()
        break

# time.sleep(2)
# print(driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value"))

#assert driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value") == "India"
assert driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value").strip().lower() == "india"
