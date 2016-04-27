from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    w3SchoolsUrl = 'http://www.w3schools.com/'
    w3SchoolsLogo = (By.XPATH, "//a[@class='w3schools-logo' and @href='http://www.w3schools.com']")
    htmlRowLocator = (By.XPATH, "//div[@class='w3-row']//h1[.='HTML']/..")
    cssRowLocator = (By.XPATH, "//div[contains(@class,'w3-row')]//h1[.='CSS']/..")
    javascriptRowLocator = (By.XPATH, "//div[@class='w3-row']//h1[.='JavaScript']/..")
    sqlRowLocator = (By.XPATH, "//div[@class='w3-row w3-light-grey']//h2[.='SQL']/..")
    phpRowLocator = (By.XPATH, "//div[@class='w3-row w3-light-grey']//h2[.='PHP']/..")
    jQueryRowLocator = (By.XPATH, "//div[@class='w3-row w3-light-grey']//h2[.='jQuery']/..")
    w3CssRowLocator = (By.XPATH, "//div[@class='w3-row']//h2[.='W3.CSS']/..")
    colorPickerRowLocator = (By.XPATH, "//div[@class='w3-row']//h2[.='Color Picker']/..")
    bootstrapRowLocator = (By.XPATH, "//div[@class='w3-row']//h2[.='Bootstrap']/..")