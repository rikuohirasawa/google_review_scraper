import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from requests_html import HTMLSession
import chromedriver_binary
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv
import math
import json
from pyvirtualdisplay import Display

def launchChrome():
    display = Display(visible=0, size=(1920,1080))
    display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/97.0.4692.71 Safari/537.36')
    driver = webdriver.Chrome(service=Service("/home/ubuntu/chromedriver"), options=chrome_options)
    driver.get('https://www.google.com/search?q=King%27s+Bridge+Service+Station%2C+Kings+Bridge+Road%2C+St.+John%27s%2C+Newfoundland+and+Labrador&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzWEZtCvuBvQYFsUhYAy_WMWmvIU9g%3A1677160312137&ei=eG_3Y-WCCM6nptQP8KKUyA0&oq=kings+bridge+auto+st+johns+newfoun&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgIIJjoHCCMQsAMQJzoKCAAQRxDWBBCwAzoECCMQJzoJCAAQFhAeEPEEOgsIABAWEB4Q8QQQCjoICAAQFhAeEAo6BQgAEIYDOgcIABANEIAEOgYIABAeEA06CwgAEAgQHhANEPEESgQIQRgAULcJWN0eYIYsaAFwAXgAgAGAAYgBmg2SAQQxMy40mAEAoAEByAEEwAEB&sclient=gws-wiz-serp#lrd=0x4b0ca3c1857b5645:0x7a7a0b75909dffd7,1,,,,')
    driver.set_window_size(1920, 1080)
    driver.save_screenshot('screenshot.png')
    driver.implicitly_wait(10)
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete') 
        print(driver.current_url)
        display.stop()

        driver.quit()
    except Exception as err:
        print(err)
        print('there is no element')

launchChrome()
