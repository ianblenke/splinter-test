#!/usr/bin/env python

from splinter import Browser
#browser = Browser()
browser = Browser('phantomjs')


browser.visit('http://google.com')

browser.fill('q', 'splinter - python acceptance testing for web applications')

button = browser.find_by_name('btnG')

button.click()


# Or done in one command
# browser.find_by_name('btnG').click()

#if browser.is_text_present('splinter.readthedocs.org', wait_time=5):
if browser.is_text_present('splinter.readthedocs.org'):
    print "Yes, found it! :)"
else:
    print "No, didn't find it :("

browser.quit()


