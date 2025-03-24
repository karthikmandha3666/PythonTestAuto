import unittest
from selenium import webdriver
from HtmlTestRunner import HTMLTestRunner  # Ensure correct import
import os


class MySeleniumTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

    def test_title(self):
        print("Page title is:", self.driver.title)
        self.assertIn("ProtoCommerce", self.driver.title)  # This might fail

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # Ensure the reports folder exists
    report_directory = "reports"
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    # Load test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(MySeleniumTests)

    try:
        runner = HTMLTestRunner(output=report_directory, report_name="TestReport", failfast=False)
        result = runner.run(suite)

        # Ensure report is generated even if tests fail
        if not result.wasSuccessful():
            print("⚠ Some test cases failed, but the report is still generated.")

    except Exception as e:
        print(f"❌ Error while running tests: {str(e)}")
