from datetime import date
import random
from hooks.hookup import print_
import re


class MarenaFilters:
    def __init__(self, array):
        self.values = self.spread(array)

    def filter(self, str_):
        if type(str_) is bytes:
            str_ = str_.decode('ascii')
        try:
            if str_[0] == '':
                str_ = str_[1:]
            str_ = re.sub("\r|\\r|wide|(|)|macro|()|'|\"", '', str_)
            str_ = re.sub(',', ' ', str_)
            str_ = re.sub(' mp', 'mp', str_)
            str_ = re.sub(' af', ' | af', str_)
            str_ = re.sub('LCD|lcd|LED|led', 'screen', str_)
            str_ = re.sub(' ghz', 'GHz', str_)
            str_ = re.sub('GHz', 'GHz', str_)
            str_ = re.sub(' nm', 'nm', str_)
            str_ = re.sub('powervr', 'PowerVR', str_)
            try:
                str_ = str_.replace('\\n', ' ').replace('()', '')
            except:
                pass
        except:
            pass
        return str_

    def spread(self, arr):
        final_ = {'subtitle': self.get_subtitle()}
        for k in arr:
            print(k)
            kname = k['name'].lower().strip()
            if 'launch' in kname:
                final_['release'] = self.getRDate(k)
            if 'platform' in kname:
                final_['plateform'] = self.getPlateform(k)
            if 'Display' in kname:
                final_['display'] = self.getDisplay(k)
            if 'main camera' in kname or 'maincamera' in kname:
                final_['main-camera'] = self.getCamera(k)
        return final_

    def getRDate(self, pro):
        for t in pro:
            if t == 'name':
                continue
            if 'announced' == t.strip().lower():
                return self.filter(pro[t])

    def getPlateform(self, k):
        obj_ = {}
        for t in k:
            if t == 'name':
                continue
            key = t.strip().lower()
            qtr = self.filter(k[t])
            if 'cpu' in key:
                obj_['cpu'] = qtr
            if 'gpu' in key:
                obj_['gpu'] = qtr
            if 'os' in key:
                obj_['os'] = qtr.lower()
            if 'chipset' in key:
                obj_['chipset'] = qtr
        return obj_

    def getDisplay(self, k):
        for t in k:
            if t == 'name':
                continue
            if 'type' in t.strip() or 'Type' in t.strip():
                return f"display {self.filter(k[t])}"

    def getCamera(self, k):
        for t in k:
            if 'MP' in k[t] or 'mp' in k[t]:
                qtr = k[t].lower()
                qtr = self.filter(qtr)
                return qtr
        return self.getDisplay()

    def getProcessor(self, k):
        for t in k:
            if t == 'name':
                continue
            if 'cpu' in t.decode('ascii') or 'CPU' in t:
                qtr = k[t].lower()

                qtr = self.filter(qtr)
                return qtr + ' processor'

    def get_subtitle(self):
        subtitle = [
            'level up!',
            f'smart your {date.today().year}',
            'upgrade your self',
            'be smart!',
            'untold story',
            'the apex of power',
            'master every view',
            'own your style',
            'stylized!',
            'power house!'

        ]
        return random.choice(subtitle)


if __name__ == '__main__':
    data = [{'name': 'Network', 'Technology': 'GSM / HSPA / LTE', '2G bands': 'GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM model only)', '3G bands': 'HSDPA 850 / 900 / 2100 ', '4G bands': '1, 3, 5, 7, 8, 20, 28, 38, 40, 41', 'Speed': 'HSPA 42.2/5.76 Mbps, LTE Cat4 150/50 Mbps'}, {'name': 'Launch', 'Announced': '2021, January 27', 'Status': 'Available. Released 2021, January 27'}, {'name': 'Body', 'Dimensions': '164 x 75.9 x 9.1 mm (6.46 x 2.99 x 0.36 in)', 'Weight': '206 g (7.27 oz)', 'Build': 'Glass front, plastic back, plastic frame', 'SIM': 'Single SIM (Nano-SIM) or Dual SIM (Nano-SIM, dual stand-by)'}, {'name': 'Display', 'Type': 'PLS LCD', 'Size': '6.5 inches, 102.0 cm2 (~81.9% screen-to-body ratio)', 'Resolution': '720 x 1600 pixels, 20:9 ratio (~270 ppi density)'}, {'name': 'Platform', 'OS': 'Android 10, upgradable to Android 11, One UI Core 3.1', 'Chipset': 'Mediatek MT6739W (28 nm)', 'CPU': 'Quad-core 1.5 GHz Cortex-A53', 'GPU': 'PowerVR GE8100'}, {'name': 'Memory', 'Card slot': 'microSDXC (dedicated slot)', 'Internal': '32GB 2GB RAM, 32GB 3GB RAM, 32GB 4GB RAM, 64GB 3GB RAM', '\xc2\xa0': 'eMMC 5.1'}, {
        'name': 'Main Camera', 'Dual': '13 MP, f/1.9, (wide), AF\n2 MP, f/2.4, (macro)', 'Features': 'LED flash', 'Video': '1080p@30fps'}, {'name': 'Selfie camera', 'Single': '5 MP, f/2.0', 'Video': ''}, {'name': 'Sound', 'Loudspeaker ': 'Yes', '3.5mm jack ': 'Yes'}, {'name': 'Comms', 'WLAN': 'Wi-Fi 802.11 b/g/n, Wi-Fi Direct, hotspot', 'Bluetooth': '5.1, A2DP, LE', 'GPS': 'Yes, with A-GPS, GLONASS', 'NFC': 'No', 'Radio': 'FM radio', 'US': 'microUSB 2.0'}, {'name': 'Features', 'Sensors': 'Accelerometer', '\xc2\xa0': 'Virtual proximity sensing'}, {'name': 'Battery', 'Type': 'Li-Po 5000 mAh, non-removable'}, {'name': 'Misc', 'Colors': 'Black, Blue', 'Models': 'SM-A022F, SM-A022F/DS, SM-A022M, SM-A022M/DS, SM-A022G, SM-A022G/DS', 'SAR EU': '0.65 W/kg (head) \xc2\xa0 \xc2\xa0 1.71 W/kg (body) \xc2\xa0 \xc2\xa0 ', 'Price': '$\xe2\x80\x89109.00 / \xe2\x82\xac\xe2\x80\x89169.00 / \xc2\xa3\xe2\x80\x89118.99 / C$\xe2\x80\x89189.00 / Rp\xe2\x80\x891,505,000'}]
    m = MarenaFilters(data)
    print(m.values)
