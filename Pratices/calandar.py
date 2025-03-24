from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")  # Replace with your calendar URL
driver.maximize_window()

# Wait until the date input field is visible and then click it
date_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-control"))
)
date_input.click()

# Select a specific date (e.g., 15th March 2025)
year = "2025"
month = "March"
day = "15"

# Select Year (if the calendar supports it)
while True:
    current_year = driver.find_element(By.CLASS_NAME, "datepicker-switch").text
    if current_year == year:
        break
    driver.find_element(By.CLASS_NAME, "next").click()  # Click next year button

# Select Month
month_elements = driver.find_elements(By.CLASS_NAME, "month")
for elem in month_elements:
    if elem.text == month[:3]:  # Short form "Mar" for March
        elem.click()
        break

# Select Day
day_elements = driver.find_elements(By.CLASS_NAME, "day")
for elem in day_elements:
    if elem.text == day:
        elem.click()
        break

# Verify Selected Date
selected_date = date_input.get_attribute("value")
print(f"Selected Date: {selected_date}")

# Close the browser
driver.quit()
