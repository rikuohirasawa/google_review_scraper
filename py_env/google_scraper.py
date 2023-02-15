import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from requests_html import HTMLSession
import chromedriver_binary
link = 'https://www.google.com/search?q=kings+bridge+auto&rlz=1C5GCEM_enCA1032CA1032&sxsrf=AJOqlzWrO_2TEnEQwAbmqIhLRgBTqz-Dmw%3A1676307742594&ei=Hm3qY73vI7CdptQPpMCYwAc&ved=0ahUKEwi99p_8_JL9AhWwjokEHSQgBngQ4dUDCA8&uact=5&oq=kings+bridge+auto&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIQCC4QgAQQFBCHAhDHARCvATILCAAQFhAeEPEEEAoyCwgAEBYQHhDxBBAKMgsIABAWEB4Q8QQQCjIICAAQFhAeEAoyAggmMgUIABCGAzIFCAAQhgM6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQqgdYqgdgsgloAnABeACAAYQBiAGEAZIBAzAuMZgBAKABAcgBBMABAQ&sclient=gws-wiz-serp#lrd=0x4b0ca3c1857b5645:0x7a7a0b75909dffd7,1,,,,'


# chrome_driver_path = '/Users/Rikuo/Downloads/chromedriver_mac_arm64/chromedriver'

def get_review(node):
    return


def launchChrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.maximize_window()
    url = "https://www.google.com/maps/place/King's+Bridge+Service+Station/@47.577349,-52.7063888,17z/data=!4m8!3m7!1s0x4b0ca3c1857b5645:0x7a7a0b75909dffd7!8m2!3d47.577349!4d-52.7042001!9m1!1b1!16s%2Fg%2F1tf7x970"
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    nodes = soup.find_all("div", class_="gws-localreviews__google-review")
    review_list = []
    # node = BeautifulSoup(str(nodes[0]), 'html.parser')
    
    for node in nodes:
        node = BeautifulSoup(str(node), 'html.parser')
        img_node = node.find("img", class_='lDY1rd')
        avatar = img_node['src']
        user_name = img_node['alt']
        rating = node.find("span", class_=['Fam1ne', 'EBe2gf'])['aria-label']
        date = node.find('span', class_=['dehysf', 'lTi8oc']).text
        content = str(node.find('div', class_='Jtu6Td'))
        review_dict = {
            'avatar': avatar,
            'name': user_name,
            'rating': rating,
            'date': date,
            'content': content
        }
        review_list.append(review_dict)

        print(content)
    
    # print(review_list)
    return review_list

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

launchChrome()
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





