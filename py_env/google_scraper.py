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



link = 'https://www.google.com/search?q=kings+bridge+auto&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzWrO_2TEnEQwAbmqIhLRgBTqz-Dmw%3A1676307742594&ei=Hm3qY73vI7CdptQPpMCYwAc&ved=0ahUKEwi99p_8_JL9AhWwjokEHSQgBngQ4dUDCA8&uact=5&oq=kings+bridge+auto&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIQCC4QgAQQFBCHAhDHARCvATILCAAQFhAeEPEEEAoyCwgAEBYQHhDxBBAKMgsIABAWEB4Q8QQQCjIICAAQFhAeEAoyAggmMgUIABCGAzIFCAAQhgM6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQqgdYqgdgsgloAnABeACAAYQBiAGEAZIBAzAuMZgBAKABAcgBBMABAQ&sclient=gws-wiz-serp#lrd=0x4b0ca3c1857b5645:0x7a7a0b75909dffd7,1,,,,'
max = 'https://www.google.com/search?q=max+auto+repairs&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzXEQpc-DPoqhQxk58HrP-hncDJ4Ag%3A1676570233806&ei=eW7uY_XRMISZptQPuYO3iAY&ved=0ahUKEwi18ufpzpr9AhWEjIkEHbnBDWEQ4dUDCA8&uact=5&oq=max+auto+repairs&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyCQgAEBYQHhDxBDIJCAAQFhAeEPEEMgYIABAWEB4yBggAEBYQHjIJCAAQFhAeEPEEMgkIABAWEB4Q8QQyCQgAEBYQHhDxBDIGCAAQFhAeMgYIABAWEB46BwgjELADECc6CggAEEcQ1gQQsAM6BAgjECc6CwguEMcBEK8BEJECOgUIABCRAjoLCC4QgAQQxwEQ0QM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoFCC4QkQI6BAgAEEM6CggAELEDEIMBEEM6EAguEIAEEBQQhwIQxwEQrwE6CwguEIAEEMcBEK8BOgQILhBDOgcILhCxAxBDOhEILhCABBCxAxCDARDHARCvAToKCC4QsQMQgwEQQzoLCC4QrwEQxwEQgARKBAhBGABQmkhYwVhg9FloCXABeACAAagBiAGqD5IBBDAuMTaYAQCgAQHIAQPAAQE&sclient=gws-wiz-serp#lrd=0x4b0ca7c55c15d4b3:0x80aada1a73c25827,1,,,,'

cred = credentials.Certificate('firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mm-scraper-db-1f403-default-rtdb.firebaseio.com'
})

def launchChrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.google.com/maps/place/King's+Bridge+Service+Station/@47.577349,-52.7063888,17z/data=!4m8!3m7!1s0x4b0ca3c1857b5645:0x7a7a0b75909dffd7!8m2!3d47.577349!4d-52.7042001!9m1!1b1!16s%2Fg%2F1tf7x970"
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-sort-id='newestFirst']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-sort-id='newestFirst']")))
    driver.find_element(By.CSS_SELECTOR, "div[data-sort-id='newestFirst']").click()
    sleep(2)
    newest_btn = driver.find_element(By.CSS_SELECTOR, "div[data-sort-id='newestFirst']")
    is_sorted_by_newest = newest_btn.get_attribute('aria-checked')
    num_reviews = int(driver.find_element(By.CSS_SELECTOR, "span[class='z5jxId']").text.split()[0])
    num_scroll_to_bottom = math.ceil(num_reviews/10)
    for i in range(0, num_scroll_to_bottom):
        driver.execute_script("document.querySelector('.review-dialog-list').scrollTo(0, document.querySelector('.review-dialog-list').scrollHeight)")
        sleep(2)
    sleep(3)
    
    scroll_modal = driver.find_element(By.CSS_SELECTOR, "div[class='review-dialog-list']")
    # print('yo', scroll_modal.scroll)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-sort-id='newestFirst' and aria-checked='true']")))

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    nodes = soup.find_all("div", class_="gws-localreviews__google-review")
    review_list = []
    for node in nodes:
        node = BeautifulSoup(str(node), 'html.parser')
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
        # print (services)
        # if review is long enough that it is clipped, get full review node
        full_text = content_soup.find('span', class_='review-full-text')
        if (full_text):
            if (services):
                content_dict['review'] = full_text.text.replace(services.text, '')
                content_dict['services'] = services.text
                # print(content_dict['review'])
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
            'full_node': str(node)
        }
        review_list.append(review_dict)    
    print(len(review_list))
    # ref.set(review_list)
    # while(True):
    #     pass
    return review_list


# print(launchChrome())




# ref = db.reference('/max_auto_repair')

def db_set(ref):
    db.reference(ref).set(launchChrome())

db_set('/kings_bridge_auto')

def db_get(ref):
    print(db.reference(ref).get())
    return db.reference(ref).get()

# print(db_get())



    # get avatar and name from img alt text

    # get review 
    # review = node.find('div', class_='Jtu6Td')
    # if (node.find('span', class_='review-full-text')):
    #     review = node.find('span', class_='review-full-text')
    # else:
    #     review = 
    # print(len(nodes))
    # for node in nodes:
    #     print(node.find())
    #     print(BeautifulSoup(node, 'html.parser').prettify())
    # for node in nodes:
    #     re_soup = BeautifulSoup(node, 'html.parser')
    #     avatar = re_soup.find("img", class_="lDY1rd")['src']
    #     print(avatar)
    # print(nodes[0])
    # for node in nodes:
    #     print(node)
    # while(True):
    #     pass

# print(launchChrome())
# session = HTMLSession()
# sleep(3)
# response = session.get('https://www.google.com/search?q=kings+bridge+auto&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzWrO_2TEnEQwAbmqIhLRgBTqz-Dmw%3A1676307742594&ei=Hm3qY73vI7CdptQPpMCYwAc&ved=0ahUKEwi99p_8_JL9AhWwjokEHSQgBngQ4dUDCA8&uact=5&oq=kings+bridge+auto&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIQCC4QgAQQFBCHAhDHARCvATILCAAQFhAeEPEEEAoyCwgAEBYQHhDxBBAKMgsIABAWEB4Q8QQQCjIICAAQFhAeEAoyAggmMgUIABCGAzIFCAAQhgM6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQqgdYqgdgsgloAnABeACAAYQBiAGEAZIBAzAuMZgBAKABAcgBBMABAQ&sclient=gws-wiz-serp#lrd=0x4b0ca3c1857b5645:0x7a7a0b75909dffd7,1,,,,')
# response.html.render()
# print(response.text)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# response = requests.get(link, timeout=(5, 4))
# print(response)
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
# title = soup.find('title')
# print(title.text)
# nodes = soup.find('a', attrs={'data-async-trigger': 'reviewDialog'})
# print(nodes)
# children = nodes.findChild('span')
# print(children.text)


# for node in nodes:
#     print(node.text)





