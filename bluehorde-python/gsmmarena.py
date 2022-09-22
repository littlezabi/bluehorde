from selenium import webdriver
from selenium.webdriver.common.by import By
from driver import Driver
from selectors import selectors_marena
from hooks.hookup import writeOn, print_
from hooks.variables import SITENAME
from bs4 import BeautifulSoup as bs4
import random
import sys
import requests
import time


class Marena(Driver):
    def __init__(self):
        self.scraped_data = []
        self.readLinks()

    def start(self, url):
        self.source = self.requester(url)
        self.html = bs4(self.encode_(self.source), 'html.parser')
        data = {
            'name': self.get_title(),
            'brief_scrap': self.get_specs_breif_pattern(),
            'mobile_specs': self.get_specs(),
            'mobile_pricing': self.get_pricing()
        }
        for k in data:
            print_(data[k])

    def readLinks(self):
        with open('./assets/marena.txt') as file:
            links = file.readlines()
            for link in links:
                print_(link)
                self.start(link)
                return 1

    def requester(self, url):
        # res = requests.get(url)
        # return res.text
        driver = self.driver()
        driver.get(url)
        html = driver.page_source
        return html

    def encode_(self, str_):
        return str(str_).encode(sys.stdout.encoding, errors='replace')

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
                tric = name
                key = self.encode_(table.select('td')[0].getText())
                value = self.encode_(table.select('td')[1].getText())
                net = {
                    'name': name,
                    key: value
                }
                for k in table.find_all('tr'):
                    try:
                        key = self.encode_(k.select('td')[0].getText())
                        value = self.encode_(k.select('td')[1].getText())
                        net[key] = value
                    except Exception as e:
                        pass
                specification_list.append(net)
            except Exception as e:
                writeOn('Error Marena -> get_specs: '+str(e))
        return specification_list

    def get_specs_breif_pattern(self):
        src = self.html.select('.center-stage')[0]
        specs = src.select('.specs-brief')[0]
        specs = specs.select('span')
        try:
            rel = specs[1].getText()
        except:
            rel = False
        try:
            thi = specs[3].getText()
        except:
            thi = False
        try:
            os = specs[5].getText()
        except:
            os = False
        try:
            sto = specs[7].getText()
        except:
            False
        try:
            rex = src.select('.specs-spotlight-features')[0]
        except:
            rex = False
        # popularity
        try:
            popu = rex.select('.help-popularity')[0].select('strong.accent')[0]
        except:
            popu = False
        popu = float(popu.getText().replace('%', ''))
        # fans and clients clicks
        try:
            fans = random.randint(400, 2000)
        except:
            fans = False
        try:
            hits = random.randint(400000, 9999999)
        except:
            False
        # display size
        try:
            dpsze = src.select('strong.accent')[2]
            dpsze = dpsze.getText().replace('"', '')
        except:
            dpsze = False
        try:
            dpsze = float(dpsze)
        except:
            pass
        try:
            dppxl = src.select('div')[1].getText()
        except:
            dppxl = False
        # camera
        try:
            fcmrp = src.select(
                '.accent.accent-camera')[0].getText()
        except:
            fcmrp = False
        try:
            vidsze = src.select('div')[2].getText()
        except:
            vidsze = False
        # memory
        try:
            mem = src.select(
                '.accent.accent-expansion')[0].getText()
        except:
            mem = False

        try:
            chipset = src.select('div')[3].getText()
        except:
            chipset = False
        # battery
        try:
            btr = src.select('.accent.accent-battery')[0].getText()
        except:
            btr = False
        try:
            btrTp = src.select('div')[4].getText()
        except:
            btrTp = False
        return {
            'title': self.get_title(),
            'released': rel,
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
            title = self.html.select(
                '.review-header')[0].select('.article-info-line')[0]
            title = title.find('h1')
            title = title.getText()
        except:
            title = self.html.select('h1')
            title = title.getText()
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
