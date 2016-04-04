import unittest
from Pages import HomePage
from splinter import Browser

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.BrowserSession = Browser('firefox')
        self.BrowserSession.driver.maximize_window()
        self.BrowserSession.visit('http://www.indeed.com')

    def test_IndeedHomePageContent(self):
        homepage = HomePage(self.BrowserSession)
        homepage.home_page_should_be_loaded()
        homepage.validate_home_page_form_content()
        homepage.validate_home_page_welcome_content()
        homepage.validate_home_page_global_nav_content()
        homepage.validate_home_page_footer_content()

    def test_simpleSearch(self):
        homepage = HomePage(self.BrowserSession)
        homepage.home_page_should_be_loaded()
        homepage.simple_job_search()


    def tearDown(self):
        self.BrowserSession.quit()