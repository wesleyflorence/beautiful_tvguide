#!/usr/bin/python3

import urllib.request
import firebase_admin
from firebase_admin import credentials, db
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import bs4 as bs
import os

class TvGuideScraper():
    tv_guide_page = 'https://www.tvguide.com/listings/'

    #Selenium stuff
    def get_dynamic_html(self):
        options = Options()
        options.headless = True
        capability = DesiredCapabilities.FIREFOX
        capability["pageLoadStrategy"] = "none"
        driver = webdriver.Firefox(options=options)
        wait = WebDriverWait(driver, 20)
        driver.get(TvGuideScraper.tv_guide_page)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'listings-channel-row')))
        driver.execute_script("window.stop();")
        html = driver.page_source
        driver.quit()
        return html

    #soup
    def scrape(self):
        here = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(here, './ServiceAccountKey.json')
        cred = credentials.Certificate(filename)
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://chatapp-a4018.firebaseio.com/'
        })
        ref = db.reference('/shows')

        html = self.get_dynamic_html()
        
        soup = bs.BeautifulSoup(html, "lxml")
        content_list = soup.find('ul', {'class':'listings-grid'})

        data = {}
        # show_dict = {}
        i = 0
        for item in content_list.find_all('li'):
            if item['class'][0] == 'listings-channel-row':
                channel = str(item['data-channel-name']).upper()
                show = item.contents[1]['data-program-title']
                show_dict = {}
                show_dict["channel"] = channel
                show_dict["show"] = show
                data[i] = show_dict
                i += 1
        ref.set(data)
        print("Firebase database updated with current shows!\n")



tv = TvGuideScraper()
tv.scrape()
