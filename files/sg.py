#!/usr/bin/env python

import re
import urlparse

from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

browser = Browser('phantomjs')

link = 'http://www.succulentguide.com/'

class SucculentScraper(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def scrape_succulent_links(self):
        self.driver.get(link)

        succulents = []

        s = BeautifulSoup(self.driver.page_source, "html.parser")
        r = re.compile(r'\?family=')
        print "@@@@@@@@@@@"
        for a in s.findAll('a', href=r):
                print "AAAAA= %s" % a
                print a['href']
                print a.text
                print "@@@"
                succulent = {}
                succulent['title'] = a.text
                succulent['url'] = urlparse.urljoin(link, a['href'])
                succulents.append(succulent)

        return succulents

    def scrape_succulent_descriptions(self, succulents):
        for succulent in succulents:
            self.driver.get(succulent['url'])            

            s = BeautifulSoup(self.driver.page_source, "html.parser")
            x = {'class': 'mastercontentpanel3'}
            d = s.find('div', attrs=x)

            if not d:
                continue

            succulent['desc'] = ' '.join(d.findAll(text=True))
            sleep(.75)

    def scrape(self):
        succulents = self.scrape_succulent_links()
        for succulent in succulents:
            print "SUCCULENTS "
            print succulent

        self.driver.quit()

if __name__ == '__main__':
    scraper = SucculentScraper()
    scraper.scrape()

