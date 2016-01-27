from splinter import Browser
browser = Browser('firefox')

browser.visit("www.python.org")
assert "Python" in browser.title

browser.fill('q','pycon')
assert browser.is_text_not_present("No results found.")