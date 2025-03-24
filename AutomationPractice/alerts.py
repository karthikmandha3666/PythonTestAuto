from selenium import webdriver
from selenium.webdriver.common.by import By

Name = "KAraThiK"
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(Name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert Name in alert_text
alert.accept()