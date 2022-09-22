from datetime import datetime
from selenium.webdriver.common.by import By


def print_(str_):
    print('______________________')
    print()
    print(str_)
    print()
    print('______________________')


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
