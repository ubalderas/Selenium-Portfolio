from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    FIND_JOBS_BTN = (By.CLASS_NAME, 'input_submit')
    INDEED_LOGO = (By.XPATH, "//img[@title='Indeed job search' and @src='/images/job_search_indeed.png']")
    SEARCH_FORM = (By.ID, "jobsearch")
    WHAT_LABEL = (By.XPATH, "//form[@id='jobsearch']//label[.='what']")
    WHERE_LABEL = (By.XPATH, "//form[@id='jobsearch']//label[.='where']")
    WHAT_INPUT = (By.ID, "what")
    WHERE_INPUT = (By.ID, "where")
    WHAT_CAPTION = (By.XPATH, "//form[@id='jobsearch']//label[.='job title, keywords or company name']")
    WHERE_CAPTION = (By.XPATH, "//form[@id='jobsearch']//label[.='city, state or zip code']")
    ADVANCED_SEARCH_LINK = (By.XPATH, "//form[@id='jobsearch']//a[.='Advanced Job Search' and contains(@href,'/advanced_search')]")
    POST_RESUME_LINK = (By.XPATH, "//p[@id='resPromoDisplay' and contains(.,' - It only takes a few seconds')]//a[@href='/promo/resume']//b[.='Post your resume']")
    WELCOME_MESSAGE = (By.ID, "hp_welcome_message")
    HOW_WORLD_WORKS_LINK = (By.XPATH, "//a[.='How the world works' and @href='/how-the-world-works']")
    GLOBAL_NAV_BAR = (By.ID, "g_nav")
    LEGAL_NOTICE = (By.XPATH, "//div[@id='legalNotice']//div[.='By using Indeed, you agree to our new ']")
    LEGAL_NOTICE_LINK = (By.XPATH, "//div[@id='legalNotice']//a[.='Terms' and @href='/legal#tos']")
    FIND_JOBS_LINK = (By.XPATH, "//div[@id='p_nav']//a[.='Find Jobs' and @id='jobsLink' and @href='/']")
    FIND_RESUMES_LINK = (By.XPATH, "//div[@id='p_nav']//a[.='Find Resumes' and @id='rezLink' and contains(@href,'/resumes')]")
    EMPLOYERS_LINK = (By.XPATH, "//div[@id='p_nav']//a[.='Employers / Post Job' and @id='empLink' and contains(@href,'/hire/')]")
    SIGNIN_LINK = (By.XPATH, "//div[@id='user_actions']//a[.='Sign in' and @id='userOptionsLabel' and contains(@href,'http://www.indeed.com/account/login')]")
    UPLOAD_RESUME_LINK = (By.XPATH, "//div[@id='user_actions']//a[.='Upload your resume' and contains(@href,'/promo/resume')]")
    FOOTER_BAR = (By.ID, "footerMainLinks")
    SALARIES_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='Salaries' and @href='/salary']")
    TRENDS_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='Browse Jobs' and @href='/find-jobs.jsp']")
    BROWSE_JOBS_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='Salaries' and @href='/salary']")
    WORK_AT_INDEED_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='Work at Indeed' and @href='http://www.indeed.jobs']")
    API_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='API' and @href='/publisher']")
    COUNTRIES_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='Countries' and @href='/worldwide']")
    ABOUT_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='About' and @href='/intl/en/about.html']")
    HELP_CENTER_LINK = (By.XPATH, "//div[@id='footerMainLinks']//a[.='Help Center' and @href='https://indeed.zendesk.com/hc/en-us']")
    LEGAL_LINK = (By.XPATH, "//div[@id='footerLegal']//a[.='Cookies, Privacy and Terms' and @href='/legal']")

    HOME_PAGE_MAIN_ELEMENTS = [SEARCH_FORM, INDEED_LOGO, GLOBAL_NAV_BAR, FOOTER_BAR, WELCOME_MESSAGE]
    HOME_PAGE_FORM_ELEMENTS = [WHAT_LABEL, WHAT_CAPTION, WHAT_INPUT, WHERE_LABEL, WHERE_CAPTION, WHERE_INPUT, FIND_JOBS_BTN, ADVANCED_SEARCH_LINK]
    HOME_PAGE_WELCOME_ELEMENTS = [POST_RESUME_LINK, HOW_WORLD_WORKS_LINK]
    HOME_PAGE_GLOBAL_NAV_ELEMENTS = [FIND_JOBS_LINK, FIND_RESUMES_LINK, EMPLOYERS_LINK, UPLOAD_RESUME_LINK, SIGNIN_LINK]
    HOME_PAGE_FOOTER_ELEMENTS = [SALARIES_LINK, TRENDS_LINK, BROWSE_JOBS_LINK, WORK_AT_INDEED_LINK, API_LINK, COUNTRIES_LINK, ABOUT_LINK, HELP_CENTER_LINK, LEGAL_LINK]

