from datetime import datetime
from selenium.webdriver.common.by import By
from hooks.variables import IMAGES_DOWNLOAD_PATH, IMAGE_PHONE_RPATH
import requests
import random
import re
import os
import time


def loading(start, text='loading...'):
    pass
    # print(text)
    # print(os.system('cls'))
    # print(text)


def getTitleFromUrl(url):
    try:
        k = url.split('/')
        k = k[len(k) - 1]
        k = k.split('-')[0]
        k = re.sub('_|-', ' ', k)
        return k
    except:
        return False


def createSlug(title):
    title = re.sub(' |_|__|--|  |"|\'', '-', title)
    title = re.sub('.php|.html', '', title)
    title = title.replace('(', '').replace(')', '')
    title = title.replace('{', '').replace('}', '')
    title = title.replace('[', '').replace(']', '')
    title = title.replace(',', '')
    title = title.replace('.', '')
    title = title.replace('--', '-')
    title = title.replace('&', 'and')
    title = title.replace('&amp;', 'and')
    title = title.lower()
    number = random.randint(99, 999)
    title = title + '-' + str(number)
    return title


def marenaTextFilter(text):
    if type(text) is bytes:
        text = text.decode('ascii')
    return text


def downloadImage(src, name):
    loading(True, 'image downloading...')
    res = requests.get(src)
    with open(IMAGES_DOWNLOAD_PATH + name, 'wb') as file:
        file.write(res.content)
    return IMAGE_PHONE_RPATH + 'a' + str(random.randint(999, 99999)) + '-' + name


def getDate():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def print_(str_):
    print('_________xxxxx_____________')
    print()
    print(str_)
    print()
    print('_________xxxxx_____________')


def writeOn(str_):
    now = datetime.now()
    now.strftime("%d/%m/%Y %H:%M:%S")
    print('[', now, '] : ', str_)


# def scrap_selector(self, selector_array, driver):
#     for selector in selector_array:
#         if selector['type'] == 'CSS_SELECTOR':
#             SELECTOR = By.CSS_SELECTOR
#         else:
#             SELECTOR = By.CSS_SELECTOR
#         try:
#             k = driver.find_element(SELECTOR, selector)
#             return k
#         except Exception as e:
#             writeOn('ERROR -> Marena.scrap_selector: ' + str(e))
