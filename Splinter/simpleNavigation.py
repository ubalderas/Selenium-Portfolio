from splinter import Browser
browser = Browser('firefox')
browser.driver.maximize_window()

browser.visit("http://www.python.org")
assert "Python" in browser.title

browser.fill('q','pycon')
assert browser.is_text_not_present("No results found.")

browser.quit()