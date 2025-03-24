import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service("D:\py\2409\chromedriver-win64\chromedriver.exe")
#service_obj = Service(r"D:\py\2409\chromedriver-win64\chromedriver.exe")
service_obj = Service("D:\\py\\2409\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://unidel.keka.com/")
print(driver.title)
print(driver.current_url)

time.sleep(2)
