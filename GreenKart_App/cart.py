import time
from http.cookiejar import lwp_cookie_str
from unittest import expectedFailure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expected_list = ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg']
Actual_list = []
driver = webdriver.Chrome()

# #Implicit Wait , for 2seconds for elements to appear
driver.implicitly_wait(2)

#Explicit Wait
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Searching the items and count
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ca")

#wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='products']/div[1]")))
#time.sleep(5)
# wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='products']/div[1]")))
wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='products']/div[5]")))

#Items_count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
Items = driver.find_elements(By.XPATH, "//div[@class='products']/div")

Items_count = len(Items)
print(f"Items found: {Items_count}")
for items in Items:
    print(items.text)
# for item in Items:
#     item_name = item.text
#     if "ca" in item_name:
#         print(item_name)
# #assert Items_count == 4
assert Items_count == 4, f"Expected 4 items, but found {Items_count}"
#buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in Items:
    Actual_list.append(button.find_element(By.XPATH, "h4").text)
    button.find_element(By.XPATH, "div/button").click()

assert expected_list == Actual_list
print(f"Actual : {Actual_list}")
print(f"list : {expected_list}")
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH,"//div[@class='cart-preview active']/div/button").click()

#appling promocode
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-last-child(1) p")
#By.XPATH, "//table[@id='productCartTables']/tbody/tr/td[5]"

sum_items = 0
for price in prices:
    sum_items = sum_items + int(price.text)
print(sum_items)
total_items = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
print(total_items)
assert sum_items == total_items

discount_amount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

assert total_items > discount_amount

driver.quit()