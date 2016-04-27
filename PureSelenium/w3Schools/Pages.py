from locators import HomePageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    """Home page action methods come here"""

    def home_page_should_be_loaded(self):
        """Verifies that the Home Page contains the main elements"""
