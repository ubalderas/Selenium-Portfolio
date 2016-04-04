from locators import HomePageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, BrowserSession):
        self.BrowserSession = BrowserSession

class HomePage(BasePage):
    """Home page action methods come here"""

    def home_page_should_be_loaded(self):
        """Verifies that the Home Page contains the main elements"""

        for element in HomePageLocators.HOME_PAGE_MAIN_ELEMENTS:
            assert self.BrowserSession.find_by_css(element).visible

    def validate_home_page_form_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_FORM_ELEMENTS:
            assert self.BrowserSession.find_by_xpath(element).visible

    def validate_home_page_welcome_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_WELCOME_ELEMENTS:
            assert self.BrowserSession.find_by_xpath(element).visible

    def validate_home_page_global_nav_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_GLOBAL_NAV_ELEMENTS:
            assert self.BrowserSession.find_by_xpath(element).visible

    def validate_home_page_footer_content(self):
        """Verifies specific text, labels and links on the page"""
        for element in HomePageLocators.HOME_PAGE_FOOTER_ELEMENTS:
            assert self.BrowserSession.find_by_xpath(element).visible

    def simple_job_search(self):
        """Performs a simple job search"""
        self.BrowserSession.find_by_xpath(HomePageLocators.WHAT_INPUT).type('Software Engineer')
        self.BrowserSession.find_by_xpath(HomePageLocators.FIND_JOBS_BTN).click()