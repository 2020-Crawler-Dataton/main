# Copyright (C) 2020-2021 github.com/can019
# Autor: Same as repo's owner
# Contact: email-jys01012@gmail.com

""" ---------------------------- import settings ----------------------------"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dateutil.parser import parse
import time

""" ------------------------------------------------------------------------"""


""" ------------------------------ Method area ------------------------------"""
# This function will become a method of ChromeExecutor
def auto_alert_accept(driver: webdriver):
    """Checking js-alert and accpet

    This method wrapped by try-catch block.
    Except: NoAlertPresentException
    return values: No exception = True, Exception occured = False
    """
    try:
        result = driver.switch_to_alert()
        result.accept()
        return True

    except NoAlertPresentException:
        """ There was no js-alert"""
        print("There is no js-alert")
        return False
    except Exception as e:
        """ Unexpected exception"""
        print("Unexpected except")
        assert e.__class__.__name__ == 'NameError'
        return False

# This function will become a method of ChromeExecutor
def google_search(driver: webdriver, search_word:str):
    search_area = driver.find_element_by_name("q")
    search_area.clear()
    search_area.send_keys(search_word)
    search_area.submit()

def get_related_search_words(driver:webdriver):
    related_search_words = driver.find_elements_by_class_name("nVcaUb")
    for i in range(len(related_search_words)):
        print(related_search_words[i].text)
        print(type(related_search_words[i]))

def get_current_page(driver: webdriver):
    whole_element = driver.page_source

""" --------------------------------------------------------------------------"""

"""
Class ChromeExecutor.
description: ChormeExecutor acutally acts as a controller.
             If run() ends, program would expire.
"""
class ChromExecutor:
    options = None
    driver = None
    capture = None
    wait = None

    def __init__(self):
        self.options = Options()
        self.options.add_argument('--start-fullscreen')  # 전체화면(f11 적용)

    def run(self):
        self.driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.google.com/')
        assert "Google" in self.driver.title
        google_search(self.driver, "운동")
        get_related_search_words(self.driver)
