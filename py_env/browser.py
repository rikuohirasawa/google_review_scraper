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

def launchChrome():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://main.d2l3seqs559cm7.amplifyapp.com/')
    print(driver.page_source)
    driver.quit()

launchChrome()