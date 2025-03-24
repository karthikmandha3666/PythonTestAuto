import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#ID, NAME, CLASS etc..,
Name = driver.find_element(By.NAME,"name")
#CSS Selector
Email = driver.find_element(By.CSS_SELECTOR, "input[name$='email']")
#XPATH
Password = driver.find_element(By.XPATH, "//input[@type='password']")
#Radia_Button
driver.find_element(By.ID, "exampleCheck1").click()

#Stander Dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select[class='form-control']"))
#dropdown.select_by_visible_text("Female")
dropdown.select_by_visible_text("Male")

driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.NAME,"bday").send_keys("05/25/1990")




#Values
Name.send_keys("Karthik M")
Email.send_keys("demo@gmail.com")
Password.send_keys("123456")


time.sleep(2)