from tkinter.constants import RADIOBUTTON

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

RadioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")

#print(len(RadioButtons)) # Its only Numbers
# Print the number of radio buttons found
print(f"Found {len(RadioButtons)} radio buttons.")


for checkbox in RadioButtons:
    if checkbox.get_attribute("value") == "radio3":
        checkbox.click()
        assert checkbox.is_selected()  # Assert that the radio button is selected after clicking
        print("Radio button with value 'radio3' is selected.")
        break