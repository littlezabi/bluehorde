from datetime import date
import random
from hooks.hookup import print_
import re


class MarenaFilters:
    def __init__(self, array):
        self.values = self.spread(array)

    def filter(self, str_):
        str_ = str(str_)
        if str_[0] == 'b':
            str_ = str_[1:]
        str_ = re.sub("\r|\\r|wide|(|)|macro|()|'|\"", '', str_)
        str_ = re.sub(',', ' ', str_)
        str_ = str_.replace('\\n', ' ').replace('()', '')
        str_ = re.sub(' mp', 'mp', str_)
        str_ = re.sub(' af', ' | af', str_)
        str_ = re.sub('LCD|lcd|LED|led', 'screen', str_)
        str_ = re.sub(' ghz', 'GHz', str_)
        str_ = re.sub('GHz', 'GHz', str_)
        str_ = re.sub(' nm', 'nm', str_)
        str_ = re.sub('powervr', 'PowerVR', str_)

        return str_

    def spread(self, arr):
        final_ = {'subtitle': self.get_subtitle()}
        for k in arr:
            print(k)
            kname = k['name'].lower().strip()
            if b'launch' in kname:
                final_['release'] = self.getRDate(k)
            if b'platform' in kname:
                final_['plateform'] = self.getPlateform(k)
            if b'Display' in kname:
                final_['display'] = self.getDisplay(k)
            if b'main camera' in kname or b'maincamera' in kname:
                final_['main-camera'] = self.getCamera(k)
        return final_

    def getRDate(self, pro):
        for t in pro:
            if t == 'name':
                continue
            if b'announced' in t.strip().lower():
                return self.filter(pro[t])

    def getPlateform(self, k):
        obj_ = {}
        for t in k:
            if t == 'name':
                continue
            key = t.strip().lower()
            qtr = self.filter(k[t])
            if b'cpu' in key:
                obj_['cpu'] = qtr
            if b'gpu' in key:
                obj_['gpu'] = qtr
            if b'os' in key:
                obj_['os'] = qtr.lower()
            if b'chipset' in key:
                obj_['chipset'] = qtr
        return obj_

    def getDisplay(self, k):
        for t in k:
            if t == 'name':
                continue
            if b'type' in t.strip() or b'Type' in t.strip():
                return f"display {self.filter(k[t])}"

    def getCamera(self, k):
        for t in k:
            if b'MP' in k[t] or b'mp' in k[t]:
                qtr = k[t].lower()
                qtr = self.filter(qtr)
                return qtr
        return self.getDisplay()

    def getProcessor(self, k):
        for t in k:
            if t == 'name':
                continue
            if b'cpu' in t or b'CPU' in t:
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
    data = [{'name': b'Network', b'Technology': b'GSM / HSPA / LTE', b'2G bands': b'GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM model only)', b'3G bands': b'HSDPA 850 / 900 / 2100 ', b'4G bands': b'1, 3, 5, 7, 8, 20, 28, 38, 40, 41', b'Speed': b'HSPA 42.2/5.76 Mbps, LTE Cat4 150/50 Mbps'}, {'name': b'Launch', b'Announced': b'2021, January 27', b'Status': b'Available. Released 2021, January 27'}, {'name': b'Body', b'Dimensions': b'164 x 75.9 x 9.1 mm (6.46 x 2.99 x 0.36 in)', b'Weight': b'206 g (7.27 oz)', b'Build': b'Glass front, plastic back, plastic frame', b'SIM': b'Single SIM (Nano-SIM) or Dual SIM (Nano-SIM, dual stand-by)'}, {'name': b'Display', b'Type': b'PLS LCD', b'Size': b'6.5 inches, 102.0 cm2 (~81.9% screen-to-body ratio)', b'Resolution': b'720 x 1600 pixels, 20:9 ratio (~270 ppi density)'}, {'name': b'Platform', b'OS': b'Android 10, upgradable to Android 11, One UI Core 3.1', b'Chipset': b'Mediatek MT6739W (28 nm)', b'CPU': b'Quad-core 1.5 GHz Cortex-A53', b'GPU': b'PowerVR GE8100'}, {'name': b'Memory', b'Card slot': b'microSDXC (dedicated slot)', b'Internal': b'32GB 2GB RAM, 32GB 3GB RAM, 32GB 4GB RAM, 64GB 3GB RAM', b'\xc2\xa0': b'eMMC 5.1'}, {
        'name': b'Main Camera', b'Dual': b'13 MP, f/1.9, (wide), AF\n2 MP, f/2.4, (macro)', b'Features': b'LED flash', b'Video': b'1080p@30fps'}, {'name': b'Selfie camera', b'Single': b'5 MP, f/2.0', b'Video': b''}, {'name': b'Sound', b'Loudspeaker ': b'Yes', b'3.5mm jack ': b'Yes'}, {'name': b'Comms', b'WLAN': b'Wi-Fi 802.11 b/g/n, Wi-Fi Direct, hotspot', b'Bluetooth': b'5.1, A2DP, LE', b'GPS': b'Yes, with A-GPS, GLONASS', b'NFC': b'No', b'Radio': b'FM radio', b'USB': b'microUSB 2.0'}, {'name': b'Features', b'Sensors': b'Accelerometer', b'\xc2\xa0': b'Virtual proximity sensing'}, {'name': b'Battery', b'Type': b'Li-Po 5000 mAh, non-removable'}, {'name': b'Misc', b'Colors': b'Black, Blue', b'Models': b'SM-A022F, SM-A022F/DS, SM-A022M, SM-A022M/DS, SM-A022G, SM-A022G/DS', b'SAR EU': b'0.65 W/kg (head) \xc2\xa0 \xc2\xa0 1.71 W/kg (body) \xc2\xa0 \xc2\xa0 ', b'Price': b'$\xe2\x80\x89109.00 / \xe2\x82\xac\xe2\x80\x89169.00 / \xc2\xa3\xe2\x80\x89118.99 / C$\xe2\x80\x89189.00 / Rp\xe2\x80\x891,505,000'}]
    m = MarenaFilters(data)
    print(m.values)
