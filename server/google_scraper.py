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
from db_handlers.db_get import db_get
from db_handlers.db_set import db_set

links = [
    # kings bridge auto
    ('https://www.google.com/search?q=King%27s+Bridge+Service+Station%2C+Kings+Bridge+Road%2C+St.+John%27s%2C+Newfoundland+and+Labrador&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzWEZtCvuBvQYFsUhYAy_WMWmvIU9g%3A1677160312137&ei=eG_3Y-WCCM6nptQP8KKUyA0&oq=kings+bridge+auto+st+johns+newfoun&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgIIJjoHCCMQsAMQJzoKCAAQRxDWBBCwAzoECCMQJzoJCAAQFhAeEPEEOgsIABAWEB4Q8QQQCjoICAAQFhAeEAo6BQgAEIYDOgcIABANEIAEOgYIABAeEA06CwgAEAgQHhANEPEESgQIQRgAULcJWN0eYIYsaAFwAXgAgAGAAYgBmg2SAQQxMy40mAEAoAEByAEEwAEB&sclient=gws-wiz-serp#lrd=0x4b0ca3c1857b5645:0x7a7a0b75909dffd7,1,,,,', '/kings_bridge_auto'),
    # max auto repairs
    ('https://www.google.com/search?q=NAPA+AUTOPRO+-+MAX%27S+AUTO+REPAIRS%2C+Bauline+Line%2C+Torbay%2C+NL&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzX3Sl3n2tgsnzRzANZTzfu69NqYBA%3A1677251079476&ei=B9L4Y5DIHIefptQPpbyz6A8&oq=max+auto+repair+bauline&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgIIJjoHCCMQsAMQJzoNCAAQRxDWBBDJAxCwAzoKCAAQRxDWBBCwAzoICAAQkgMQsAM6BAgjECc6BQgAEIAEOgYIABAWEB46CQgAEBYQHhDxBEoECEEYAFCkJVj7Q2DUXGgBcAF4AIABfIgBlweSAQMwLjiYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp#lrd=0x4b0ca7c55c15d4b3:0x80aada1a73c25827,1,,,,', '/max_auto_repair')
]
link = 'https://www.google.com/search?q=King%27s+Bridge+Service+Station%2C+Kings+Bridge+Road%2C+St.+John%27s%2C+Newfoundland+and+Labrador&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzWEZtCvuBvQYFsUhYAy_WMWmvIU9g%3A1677160312137&ei=eG_3Y-WCCM6nptQP8KKUyA0&oq=kings+bridge+auto+st+johns+newfoun&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgIIJjoHCCMQsAMQJzoKCAAQRxDWBBCwAzoECCMQJzoJCAAQFhAeEPEEOgsIABAWEB4Q8QQQCjoICAAQFhAeEAo6BQgAEIYDOgcIABANEIAEOgYIABAeEA06CwgAEAgQHhANEPEESgQIQRgAULcJWN0eYIYsaAFwAXgAgAGAAYgBmg2SAQQxMy40mAEAoAEByAEEwAEB&sclient=gws-wiz-serp#lrd=0x4b0ca3c1857b5645:0x7a7a0b75909dffd7,1,,,,'
max = 'https://www.google.com/search?q=max+auto+repairs&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzXEQpc-DPoqhQxk58HrP-hncDJ4Ag%3A1676570233806&ei=eW7uY_XRMISZptQPuYO3iAY&ved=0ahUKEwi18ufpzpr9AhWEjIkEHbnBDWEQ4dUDCA8&uact=5&oq=max+auto+repairs&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyCQgAEBYQHhDxBDIJCAAQFhAeEPEEMgYIABAWEB4yBggAEBYQHjIJCAAQFhAeEPEEMgkIABAWEB4Q8QQyCQgAEBYQHhDxBDIGCAAQFhAeMgYIABAWEB46BwgjELADECc6CggAEEcQ1gQQsAM6BAgjECc6CwguEMcBEK8BEJECOgUIABCRAjoLCC4QgAQQxwEQ0QM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoFCC4QkQI6BAgAEEM6CggAELEDEIMBEEM6EAguEIAEEBQQhwIQxwEQrwE6CwguEIAEEMcBEK8BOgQILhBDOgcILhCxAxBDOhEILhCABBCxAxCDARDHARCvAToKCC4QsQMQgwEQQzoLCC4QrwEQxwEQgARKBAhBGABQmkhYwVhg9FloCXABeACAAagBiAGqD5IBBDAuMTaYAQCgAQHIAQPAAQE&sclient=gws-wiz-serp#lrd=0x4b0ca7c55c15d4b3:0x80aada1a73c25827,1,,,,'

cred = credentials.Certificate('firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mm-scraper-db-1f403-default-rtdb.firebaseio.com/'
})

def launchChrome(url, db_ref):
    print(db_ref)

    try:
        # display = Display(visible=0, size=(1920, 1080))
        # display.start()
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/97.0.4692.71 Safari/537.36')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()
        driver.get(url)
        print('url received')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-sort-id='newestFirst']")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-sort-id='newestFirst']")))
        driver.find_element(By.CSS_SELECTOR, "div[data-sort-id='newestFirst']").click()
        print('clicked btn')
        sleep(2)
        num_reviews = int(driver.find_element(By.CSS_SELECTOR, "span[class='z5jxId']").text.split()[0])
        num_scroll_to_bottom = math.ceil(num_reviews/10)
        for i in range(0, num_scroll_to_bottom):
            driver.execute_script("document.querySelector('.review-dialog-list').scrollTo(0, document.querySelector('.review-dialog-list').scrollHeight)")
            sleep(2)
        print('scrolled to bottom')
        sleep(3)
        
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        nodes = soup.find_all("div", class_="gws-localreviews__google-review")
        review_list = []
        for node in nodes:
            node = BeautifulSoup(str(node), 'html.parser')
            # trim down the nodes, removing unecessary nodes
            # node.find("g-dropdown-menu").decompose()
            # removals = node.find_all("g-snackbar")
            # for rm in removals:
            #     rm.decompose()
            # node.find("span", class_="review-snippet").decompose()
            img_node = node.find("img", class_='lDY1rd')
            avatar = img_node['src']
            user_name = img_node['alt']
            rating = node.find("span", class_=['Fam1ne', 'EBe2gf'])['aria-label']
            date = node.find('span', class_=['dehysf', 'lTi8oc']).text
            
            content_dict = {
                'review': '',
                'services': ''
            }
            content = node.find('div', class_='Jtu6Td')
            content_soup = BeautifulSoup(str(content), 'html.parser')
            # services - if customer lists services they received
            services = content_soup.find('div', class_='JRGY0')
            if (services == None):
                services = content_soup.find('div', class_='eX1cmf')
            reply_list = []
            # owner responses
            reply_node = node.find('div', class_='LfKETd')
            if (reply_node):
                reply = {
                    'date': '',
                    'content': ''
                }

                if (BeautifulSoup(str(reply_node), 'html.parser').find('div', class_='lororc')):
                    reply_soup = BeautifulSoup(str(reply_node), 'html.parser').find('div', class_='lororc')
                    reply_content_node = reply_soup.find('span', class_='d6SCIc')
                    reply['content'] = str(reply_content_node)
                else:
                    reply_content_node = node.find('div', class_='d6SCIc')
                    if reply_content_node:
                        reply['content'] = reply_content_node.text
                reply_date_node = node.find('span', class_='pi8uOe')
                reply['date'] = reply_date_node.text
                reply_list.append(reply)
            
            # if review is long enough that it is clipped, get full review node
            full_text = content_soup.find('span', class_='review-full-text')
            if (full_text):
                if (services):
                    content_dict['review'] = full_text.text.replace(services.text, '')
                    content_dict['services'] = services.text
                    review_text = str(full_text)
                    review_services = str(services)
                    full_text = review_text.replace(review_services, '')
                else:
                    content_dict['review'] = full_text.text
            # else if services are in review text
            elif (services):
                content_dict['review'] = content_soup.text.replace(services.text, '')
                content_dict['services'] = services.text
            # else get review content as normal
            else: 
                content_dict['review'] = content_soup.find('div', class_='Jtu6Td').text
            # services
            review_dict = {
                'avatar': avatar,
                'name': user_name,
                'rating': rating,
                'date': date,
                'content': content_dict,
                'full_review': str(full_text),
                'replies': json.dumps(reply_list)
            }
            review_list.append(review_dict)    
        print(len(review_list))
        # while(True):
        #     pass
        db_set(db_ref, review_list)
        return review_list
    except Exception as err:
        print(err.args)
        print(err)
        print(type(err))
# launchChrome()




# db_set('/kings_bridge_auto', launchChrome())

for garage in links:
    url = garage[0]
    db_ref = garage[1]
    launchChrome(url, db_ref)

# ref = db.reference('/max_auto_repair')

# def db_set(ref):
#     db.reference(ref).set(launchChrome())

# db_set('/kings_bridge_auto', launchChrome())

# def db_get(ref):
#     print(db.reference(ref).get())
#     return db.reference(ref).get()

# print(db_get('/kings_bridge_auto'))





