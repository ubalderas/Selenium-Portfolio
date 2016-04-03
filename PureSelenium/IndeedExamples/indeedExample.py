import unittest
import indeedPages
from selenium import webdriver

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://www.indeed.com")

    def test_IndeedHomePageContent(self):
        homepage = indeedPages.HomePage(self.driver)
        homepage.home_page_should_be_loaded()
        homepage.validate_home_page_form_content()
        homepage.validate_home_page_welcome_content()
        homepage.validate_home_page_global_nav_content()
        homepage.validate_home_page_footer_content()

    def tearDown(self):
        self.driver.close()