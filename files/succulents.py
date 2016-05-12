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
        pageno = 2

        while True:
            s = BeautifulSoup(self.driver.page_source, "html.parser")
#https://l3com.taleo.net/careersection/l3_ext_us/jobdetail.ftl?job=081264
#http://www.succulentguide.com/family_page/?family=Agavaceae
            r = re.compile(r'\?family=')

            for a in s.findAll('a', href=r):
                tr = a.findParent('tr')
                td = tr.findAll('td')

                succulent = {}
                succulent['title'] = a.text
                succulent['url'] = urlparse.urljoin(link, a['href'])
                succulent['location'] = td[2].text
                succulents.append(succulent)

            next_page_elem = self.driver.find_element_by_id('next')
            next_page_link = s.find('a', text='%d' % pageno)

            if next_page_link:
                next_page_elem.click()
                pageno += 1
                sleep(.75)
            else:
                break

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
            print succulent

        self.driver.quit()

if __name__ == '__main__':
    scraper = SucculentScraper()
    scraper.scrape()
