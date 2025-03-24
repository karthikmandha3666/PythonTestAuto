import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield driver
    driver.quit()

def test_title(driver):
    try:
        assert "Practice" in driver.title, "Title does not match!"
    except AssertionError:
        driver.save_screenshot("reports/failure_screenshot.png")
        raise  # Re-raise the exception to fail the test
