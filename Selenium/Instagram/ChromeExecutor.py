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
def auto_login(driver: webdriver):
    """ Auto login
    """
    str = "_2hvTZ pexuQ zyHYP"
    element = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    element.send_keys("usdk1234")
    element = driver.find_element_by_xpath('// *[ @ id = "loginForm"] / div / div[2] / div / label / input')
    element.send_keys("qwer1234!")
    element.submit()

    """
        Skip pop up options
    """
    skip_store_login_info(driver)
    skip_alarm_setting(driver)

# This function will become a method of ChromeExecutor
def skip_store_login_info(driver:webdriver):
    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    try:
        element.click()
        return True
    except Exception as e:
        print(e.__class__.__name__)
        return False

def skip_alarm_setting(driver: webdriver):
    element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    if str(element.text) != "나중에 하기":
        return True
    try:
        element.click()
        return True
    except Exception as e:
        print(e.__class__.__name__)
        return False
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
        self.driver = webdriver.Chrome('./chromedriver_win32/chromedriver_87.exe')
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.instagram.com/')
        assert "Instagram" in self.driver.title
        auto_login(self.driver)

        'sqdOP  L3NKy _4pI4F  y3zKF     '


