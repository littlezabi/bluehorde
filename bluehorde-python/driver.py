from selenium import webdriver
from paths import *


class Driver:
    def __init__(self):
        pass

    def driver(self):
        self.driver = webdriver.Chrome(executable_path=chromedriver)
        return self.driver
