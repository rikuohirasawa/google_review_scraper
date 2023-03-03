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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def launchChrome():
    # display = Display(visible=0, size=(1920,1080))
    # display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/97.0.4692.71 Safari/537.36')
    # driver = webdriver.Chrome(service=Service("/home/ubuntu/chromedriver"), options=chrome_options)
    driver = webdriver.Remote("http://0.0.0.0:4444/wd/hub", options=chrome_options)
    driver.get('https://www.google.com/search?q=King%27s+Bridge+Service+Station%2C+Kings+Bridge+Road%2C+St.+John%27s%2C+Newfoundland+and+Labrador&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzWEZtCvuBvQYFsUhYAy_WMWmvIU9g%3A1677160312137&ei=eG_3Y-WCCM6nptQP8KKUyA0&oq=kings+bridge+auto+st+johns+newfoun&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgIIJjoHCCMQsAMQJzoKCAAQRxDWBBCwAzoECCMQJzoJCAAQFhAeEPEEOgsIABAWEB4Q8QQQCjoICAAQFhAeEAo6BQgAEIYDOgcIABANEIAEOgYIABAeEA06CwgAEAgQHhANEPEESgQIQRgAULcJWN0eYIYsaAFwAXgAgAGAAYgBmg2SAQQxMy40mAEAoAEByAEEwAEB&sclient=gws-wiz-serp#lrd=0x4b0ca3c1857b5645:0x7a7a0b75909dffd7,1,,,,')
    driver.set_window_size(1920, 1080)
    sleep(5)
    driver.save_screenshot('screenshot.png')
    driver.implicitly_wait(10)
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete') 
        print(driver.current_url)
        # display.stop()

        driver.quit()
    except Exception as err:
        print(err)
        print('there is no element')

launchChrome()


# string = r"""<span class="review-full-text" style="display:none">I have never had more trust in a garage and it's staff than in Kings bridge service station.<br/><br/>Honest service with no beating around the bush.<br/>Kind knowledgable helpful crew - but don't waist there time.<br/>It's a St.John's business legacy for god"s sake.<br/>That title has been earned, not claimed.<br/><br/>I wish my truck ( though they tell me its a car)- broke down more often..thats how much time i have for this joint.<br/><br/>Ned Pratt<br/><br/>proud Honda Ridgeline owner.<br/>( it is a truck)<div class="JRGY0"><b class="YQwAz">Services:</b><span class="h5vETc"> <span>Engine repair</span>, <span>Air conditioning</span>, <span>Auto engine diagnostic</span>, <span>Tires</span>, <span>Brakes</span>, <span>Auto brake repair</span></span></div></span>"""

# services = r"""<div class="JRGY0"><b class="YQwAz">Services:</b><span class="h5vETc"> <span>Engine repair</span>, <span>Air conditioning</span>, <span>Auto engine diagnostic</span>, <span>Tires</span>, <span>Brakes</span>, <span>Auto brake repair</span></span></div>"""
# print(string.replace(services, ''))

