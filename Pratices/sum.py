from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Fill out the form
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("John Doe")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("johndoe@example.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@1234")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Wait for success message
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    assert "Successss" in success_message.text, "Form submission failed!"
    print("Test Passed: Form submitted successfully!")
except Exception as e:
    print("Test Failed:", e)

# Close browser
driver.quit()
