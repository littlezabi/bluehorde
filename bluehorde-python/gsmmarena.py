from selenium import webdriver
from selenium.webdriver.common.by import By
# from driver import Driver
from selectors import selectors_marena
from hooks.hookup import writeOn, print_, downloadImage, marenaTextFilter, getTitleFromUrl, getDate, createSlug
from hooks.variables import SITENAME, CHROMEDRIVER
from bs4 import BeautifulSoup as bs4
import random
import sys
import requests
import time
from storage.database import Mongo
from filters import MarenaFilters
from fake_useragent import UserAgent
from storage.database import Mongo


class Marena:
    def __init__(self):
        options = webdriver.ChromeOptions()

        # options.add_argument('--proxy-server=%s' % PROXY)
        # options.add_argument('--disable-gpu')
        # options.add_argument('--headless')
        options.add_argument('--user-data-dir=C:/blue-horde/')
        self.driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER, options=options)
        # time.sleep(10000)
        self.scraped_data = []
        self.ok_title = ''
        self.driver_is_live = False
        self.current_url = ''
        self.links_db = Mongo('URLs_list').modal
        self.mobile_devices_db = Mongo().modal
        self.readLinks()

    def start(self, url, id):
        self.current_url = url
        self.source = self.requester(url)
        self.html = bs4(self.encode_(self.source), 'html.parser')
        get_sbp = self.get_specs_breif_pattern()
        print(get_sbp)
        if get_sbp == 'unable-to-scrap':
            return 1
        data = {
            'name': self.get_title(),
            'brief_scrap': get_sbp,
            'mobile_specs': self.get_specs(),
            'mobile_pricing': self.get_pricing(),
            'createdAt': getDate(),
            'original': url,
            'from': 'gsmarena'
        }
        data['short_detail'] = MarenaFilters(data['mobile_specs']).values
        data['slug'] = createSlug(data['name'])
        if self.mobile_devices_db.insert_one_(data):
            self.links_db.update_one({'_id': id}, {'$set': {'scrapped': True}})
        print('Done -> ', data['slug'])

    def readLinks(self):
        links = self.links_db.find({'scrapped': False}, {
                                   'url': 1}).limit(200)
        i = 0
        for link in links:
            i += 1
            print_(f'{i} -> ' + link['url'])
            self.start(link['url'], link['_id'])

    def requester(self, url):
        # headers = UserAgent().random
        # res = requests.get(url, headers={'Content-Type': headers})
        # return res.text
        html = self.driver.get(url)
        html = self.driver.page_source
        self.source = html
        return html

    def encode_(self, str_):
        str_ = str_.encode("ascii", "ignore")
        str_ = str_.decode()
        return str_

    def get_pricing(self):
        html = self.html
        trs = html.select('table.pricing tbody tr')
        pricing_list = []
        for tr in trs:
            try:
                spec = tr.select('td')[0].getText()
                links = tr.select('td a')
                img = tr.select('td img')
                store_links = {}
                i = 0
                list_urls = []
                for link in links:
                    try:
                        anchor = link['href'].split('?tag')[0]
                        anchor = anchor.split('#gsmarena')[0]
                        anchor = anchor.split('&customid=')[0]
                        anchor = anchor.replace('=gsmarena', SITENAME)[0]
                        urt = {}
                        urt['store'] = anchor
                        try:
                            image = img[i]['src']
                            urt['logo'] = image
                        except:
                            image = img[i]['src']
                            urt['logo'] = anchor.split(
                                'https://')[1].split('/')[0]
                        list_urls.append(urt)
                        i += 1
                    except Exception as e:
                        writeOn('Error: Marena -> get_pricing ' + str(e))
                store_links['spec'] = spec
                store_links['links'] = list_urls
                pricing_list.append(store_links)
            except Exception as e:
                writeOn('Error: Marena -> get_pricing 1st exception ' + e)
        return pricing_list

    def get_specs(self):
        specification_list = []
        spec_list = self.html.select('#specs-list')[0]
        tables = spec_list.select('table')
        m = 0
        tric = ''
        for table in tables:
            try:
                name = self.encode_(table.select('th')[0].getText())
                if tric == name:
                    continue
                tric = marenaTextFilter(name)
                key = self.encode_(table.select('td')[0].getText())
                value = self.encode_(table.select('td')[1].getText())
                net = {
                    'name': marenaTextFilter(name),
                    key: marenaTextFilter(value)
                }
                for k in table.find_all('tr'):
                    try:
                        key = self.encode_(k.select('td')[0].getText())
                        value = self.encode_(k.select('td')[1].getText())
                        net[key] = marenaTextFilter(value)
                    except Exception as e:
                        pass
                specification_list.append(marenaTextFilter(net))
            except Exception as e:
                writeOn('Error Marena -> get_specs: '+str(e))
        return specification_list

    def get_specs_breif_pattern(self):
        src = self.html.select('.center-stage')[0]
        img = src.select('.specs-photo-main')[0]
        specs = src.select('.specs-brief')[0]
        specs = specs.select('span')
        try:
            img = img.select('img')[0]['src']
            try:
                img = downloadImage(img, img.split(
                    '/')[len(img.split('/')) - 1])
            except:
                pass
        except:
            img = False
        try:
            rel = marenaTextFilter(specs[1].getText())
        except:
            rel = False
        try:
            thi = marenaTextFilter(specs[3].getText())
        except:
            thi = False
        try:
            os = marenaTextFilter(specs[5].getText())
        except:
            os = False
        try:
            sto = marenaTextFilter(specs[7].getText())
        except:
            False
        try:
            rex = marenaTextFilter(src.select('.specs-spotlight-features')[0])
        except:
            rex = False
        # popularity
        try:
            popu = rex.select(
                '.help-popularity')[0].select('strong.accent')[0].getText()
            popu = popu.replace('%', '')
        except:
            popu = False
        try:
            fans = marenaTextFilter(random.randint(400, 2000))
        except:
            fans = False
        try:
            hits = random.randint(400000, 9999999)
        except:
            False
        # display size
        try:
            dpsze = src.select('strong.accent')[2]
            dpsze = marenaTextFilter(dpsze.getText().replace('"', ''))
        except:
            dpsze = False
        try:
            dpsze = float(dpsze)
        except:
            pass
        try:
            dppxl = marenaTextFilter(src.select('div')[1].getText())
        except:
            dppxl = False
        # camera
        try:
            fcmrp = marenaTextFilter(src.select(
                '.accent.accent-camera')[0].getText())
        except:
            fcmrp = False
        try:
            vidsze = marenaTextFilter(src.select('div')[2].getText())
        except:
            vidsze = False
        # memory
        try:
            mem = marenaTextFilter(src.select(
                '.accent.accent-expansion')[0].getText())
        except:
            mem = False

        try:
            chipset = marenaTextFilter(src.select('div')[3].getText())
        except:
            chipset = False
        # battery
        try:
            btr = marenaTextFilter(src.select(
                '.accent.accent-battery')[0].getText())
        except:
            btr = False
        try:
            btrTp = marenaTextFilter(src.select('div')[4].getText())
        except:
            btrTp = False
        return {
            'title': marenaTextFilter(self.get_title()),
            'released': rel,
            'image': img,
            'thickness': thi,
            'os': os,
            'storage': sto,
            'popularity': popu,
            'fans': fans,
            'hits': hits,
            'displaySize': dpsze,
            'displayPixles': dppxl,
            'frontCamera': fcmrp,
            'vidoeSize': vidsze,
            'Memory': mem,
            'Chipset': chipset,
            'battery': btr,
            'batteryType': btrTp
        }

    def get_title(self):
        try:
            try:
                title = self.html.select(
                    '.review-header')[0].select('.article-info-line')[0]
                title = title.find('h1')
                title = title.getText()
            except:
                title = self.html.select('.article-info')[0]
                title = self.html.select('h1')[0]
                title = title.getText()
        except:
            title = getTitleFromUrl(self.current_url)
        return title

    def scrap_selector(self, selector_array):
        for selector in selector_array:
            if selector['type'] == 'CSS_SELECTOR':
                SELECTOR = By.CSS_SELECTOR
            else:
                SELECTOR = By.CSS_SELECTOR
            try:
                k = self.driver.find_element(SELECTOR, selector)
                return k
            except Exception as e:
                writeOn('ERROR -> Marena.scrap_selector: ' + str(e))


if __name__ == '__main__':
    # Marena('https://www.gsmarena.com/samsung_galaxy_a32-10753.php')
    Marena()
