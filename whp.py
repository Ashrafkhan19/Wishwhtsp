from re import split

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


# importing google_images_download module
# from google_images_download import google_images_download


def love():
    url = "http://thecircular.org/say-i-love-you-in-100-languages/"

    req = requests.get(url)

    con = BeautifulSoup(req.content, 'html.parser')
    ol = con.find('ol')
    li = ol.find_all('li')
    msg = []
    wh = []

    for i in range(len(li)):
        msg.append(li[i].get_text())
        t = split('\(', msg[i])
        wh.append(t[0])
    msg.clear()
    browser: WebDriver = webdriver.Firefox('/home/emir/Downloads/geckodriver')
    browser.get('https://web.whatsapp.com/')
    input('input anything after scan QR')

    ib = browser.find_element_by_css_selector('span[title="Lata Bhabhi"]')
    ib.click()
    text = ib.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

    for i in wh:
        text.send_keys(i)
        sleep(3)
        text.send_keys(Keys.RETURN)
    browser.close()


def coach():
    Url2 = "https://truelovewords.com/sweet-birthday-wishes-for-your-girlfriend/"
    love = requests.get(Url2)

    glove = BeautifulSoup(love.content, 'html.parser')

    ul = glove.find_all('ul', class_='')

    lv = []

    print(ul[0].find('li').get_text())

    for l in ul:
        k = l.find_all('li')
        for a in range(len(k)):
            lv.append(k[a].get_text())

    URL = "https://quote.com/blog/77-perfect-love-quotes/#:~:text=Timeless%20Quotes%20About%20Love%3A&text=The%20best%20and%20most%20beautiful,be%20felt%20with%20the%20heart.&text=Life%20without%20love%20is%20like%20a%20tree%20without%20blossoms%20or%20fruit.&text=The%20best%20thing%20to%20hold%20onto%20in%20life%20is%20each%20other.&text='Tis%20better%20to%20have%20loved,to%20have%20loved%20at%20all."
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    bq = soup.find_all('blockquote', class_='pull-quote')

    q = []
    for b in bq:
        q.append(b.find('p').get_text())

    browser = webdriver.Chrome('G:\pyway\emir\chromedriver')
    browser.get('https://web.whatsapp.com/')
    input("scan QR and press any key")

    cdrm = browser.find_element_by_css_selector('span[title=""]')
    cdrm.click()

    text = cdrm.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

    for i in range(len(lv) - 34):
        text.send_keys(lv[i])
        sleep(1)
        text.send_keys(Keys.RETURN)

    browser.close()


def tps():
    msg = ['hi.... bittan', 'hui.. bittan ', 'Merhaba', 'hello']
    browser = webdriver.Chrome('G:\pyway\emir\chromedriver')
    browser.get('https://web.whatsapp.com/')
    input('input anything after scan QR')
    ib = browser.find_element_by_css_selector('span[title="Emir"]')
    ib.click()
    text = ib.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

    while True:
        text.send_keys(random.choice(msg))

        text.send_keys(Keys.RETURN)
        sleep(110)


def mamt():
    url = "https://truelovewords.com/birthday-wishes/"
    gurl = requests.get(url)
    soup = BeautifulSoup(gurl.content, 'html.parser')
    ul = soup.find_all('ul', class_='')
    msg = []
    for i in range(len(ul)):
        li = ul[i].find_all('li')
        for j in range(len(li)):
            msg.append(li[j].get_text())

    browser = webdriver.Chrome('G:\pyway\emir\chromedriver')
    browser.get('https://web.whatsapp.com/')
    input("scan QR and press any key")

    cdrm = browser.find_element_by_css_selector('span[title="Shifu"]')
    cdrm.click()
    text = cdrm.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    for i in range(len(msg) - 24):
        text.send_keys(msg[i])
        sleep(10)
        text.send_keys(Keys.RETURN)


love()

#
# def dwnldimg():
#     # creating object
#     response = google_images_download.googleimagesdownload()
#
#     search_queries = [
#
#         'The smartphone also features an in display fingerprint sensor.',
#         'The pop up selfie camera is placed aligning with the rear cameras.',
#         '''In terms of storage Vivo V15 Pro could offer
#            up to 6GB of RAM and 128GB of onboard storage.''',
#         'The smartphone could be fuelled by a 3 700mAh battery.',
#     ]
#
#     def downloadimages(query):
#         # keywords is the search query
#         # format is the image file format
#         # limit is the number of images to be downloaded
#         # print urs is to print the image file url
#         # size is the image size which can
#         # be specified manually ("large, medium, icon")
#         # aspect ratio denotes the height width ratio
#         # of images to download. ("tall, square, wide, panoramic")
#         arguments = {"keywords": query,
#                      "format": "jpg",
#                      "limit": 4,
#                      "print_urls": True,
#                      "size": "medium",
#                      "aspect_ratio": "panoramic"}
#         try:
#             response.download(arguments)
#
#             # Handling File NotFound Error
#         except FileNotFoundError:
#             arguments = {"keywords": query,
#                          "format": "jpg",
#                          "limit": 4,
#                          "print_urls": True,
#                          "size": "medium"}
#
#             # Providing arguments for the searched query
#             try:
#                 # Downloading the photos based
#                 # on the given arguments
#                 response.download(arguments)
#             except:
#                 pass
#
#     # Driver Code
#     for query in search_queries:
#         downloadimages(query)
#         print()
#
