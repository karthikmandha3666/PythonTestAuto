import pytest
from selenium import webdriver
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield driver
    driver.quit()

@allure.feature("Title Verification")
@allure.story("Check if the page title contains 'Practice'")
@allure.severity(allure.severity_level.CRITICAL)
def test_title(driver):
    """Test to check if the title contains 'Practice'"""
    with allure.step("Getting page title"):
        page_title = driver.title
        allure.attach(page_title, name="Page Title", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Validating title"):
        assert "Practice" in page_title, "Title does not match!"

@allure.feature("UI Test")
@allure.story("Capture screenshot on failure")
def test_screenshot_on_failure(driver):
    """Captures a screenshot if test fails"""
    try:
        assert "WrongTitle" in driver.title  # This will fail
    except AssertionError:
        driver.save_screenshot("reports/failure.png")
        allure.attach.file("reports/failure.png", name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        raise  # Re-raise the exception to fail the test
