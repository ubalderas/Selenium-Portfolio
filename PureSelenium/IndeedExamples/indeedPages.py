from locators import HomePageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    """Home page action methods come here"""

    def home_page_should_be_loaded(self):
        """Verifies that the Home Page contains the main elements"""
        assert "Indeed.com" in self.driver.title
        for element in HomePageLocators.HOME_PAGE_MAIN_ELEMENTS:
            assert self.driver.find_element(*element)

    def validate_home_page_form_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_FORM_ELEMENTS:
            assert self.driver.find_element(*element)

    def validate_home_page_welcome_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_WELCOME_ELEMENTS:
            assert self.driver.find_element(*element)

    def validate_home_page_global_nav_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_GLOBAL_NAV_ELEMENTS:
            assert self.driver.find_element(*element)

    def validate_home_page_footer_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_FOOTER_ELEMENTS:
            assert self.driver.find_element(*element)



