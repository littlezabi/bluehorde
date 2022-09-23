from selenium import webdriver
from paths import *


class Driver:
    def __init__(self):
        pass

    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=C:/blue-horde/')
        self.driver = webdriver.Chrome(
            executable_path=chromedriver, options=options)
        return self.driver
