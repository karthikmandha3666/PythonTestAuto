from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

products_list = driver.find_elements(By.XPATH,"//div[@class = 'card h-100']")

for product in products_list:
    if product.text == "blackberry":
        product.click()
        break



print(driver.current_url)