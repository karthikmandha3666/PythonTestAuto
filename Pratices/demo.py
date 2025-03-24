import unittest
from selenium import webdriver
# from html_testRunner import HTMLTestRunner  # Import the module
from HtmlTestRunner import HTMLTestRunner  # Use capital 'H' and 'T'


class MySeleniumTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

    def test_title(self):
        print("Page title is:", self.driver.title)
        self.assertIn("ProtCommerce", self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # Create a test suite from all test cases in MySeleniumTests
    suite = unittest.TestLoader().loadTestsFromTestCase(MySeleniumTests)

    # Create an HTMLTestRunner instance to generate an HTML report in the "reports" directory
    runner = HTMLTestRunner(output='reports')

    # Run the test suite using the HTMLTestRunner
    runner.run(suite)
