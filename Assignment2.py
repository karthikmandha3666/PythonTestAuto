import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_optn = webdriver.ChromeOptions()
chrome_optn.add_argument("headless")

driver = webdriver.Chrome(options=chrome_optn)
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 5)


driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME, "blinkingText").click()

windows_lis = driver.window_handles
driver.switch_to.window(windows_lis[1])

# email_info = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
# print(email_info)

Email_ID = driver.find_element(By.XPATH, "//a[contains(@href,'mailto:')]").text
# print("Email ID :",Email_ID)
driver.close()

driver.switch_to.window(windows_lis[0])
Username = driver.find_element(By.ID, "username")
Username.send_keys(Email_ID)
driver.find_element(By.NAME, "password").send_keys("123234")
driver.find_element(By.CSS_SELECTOR, "input[value ='user']").click()
# user = wait.until(EC.presence_of_element_located((By.ID, "okayBtn")))
# user.click()
#driver.find_element(By.ID, "okayBtn")

wait.until(EC.element_to_be_clickable((By.ID, "okayBtn"))).click()

dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_value("teach")

wait.until(EC.element_to_be_clickable((By.ID, "terms"))).click()
# wait.until(EC.presence_of_element_located((By.NAME,"terms")))
# driver.find_element(By.XPATH,"//input[@id='terms']").click()

driver.find_element(By.ID, "signInBtn").click()
error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print("Error message :",error_message.text)


driver.quit()


time.sleep(2)