# Copyright (C) 2020-2021 github.com/can019
# Autor: Same as repo's owner
# Contact: email-jys01012@gmail.com

""" ---------------------------- import settings ----------------------------"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dateutil.parser import parse
import time
import CapturingAndParsing

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
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    try:
        element.click()
        return True
    except Exception as e:
        print(e.__class__.__name__)
        return False
# This function will become a method of ChromeExecutor
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
# def follow_influencers_by_recomendation_option2(driver: webdriver):
#     try:
#     except Exception as e:
#         print(e.__class__.__name__)
#         print(e)
#
# def follow_influencers_by_recomendation_option1(driver: webdriver):
#     recommendation_div = driver.find_element_by_xpath \
#         ('// *[ @ id = "react-root"] / section / main / section / div / div[2] / div / div / div[2] / div / div / div')
#     profile_links = recommendation_div.find_elements_by_tag_name('a')
#
#     recommendation_div = driver.find_element_by_xpath \
#         ('//*[@id="react-root"]/section/main/section/div/div[3]/div/div/div[2]/div/div')
#     profile_links = recommendation_div.find_elements_by_tag_name('a')
#     for i in range(len(profile_links)):
#         profile_links[i].click()
#         g47SY[1] -> 팔로워
#         수
#         .이
#         없는
#         경우
#         pass
#     (mTLOB Szr5J coreSpriteVerifiedBadge)-> 뱃지
#     try:
#         recommendation_div = driver.find_element_by_xpath \
#             ('// *[ @ id = "react-root"] / section / main / section / div / div[2] / div / div / div[2] / div / div / div')
#         follow_buttons = recommendation_div.find_elements_by_tag_name('button')
#         for i in range(len(follow_buttons)):
#             threshhold = 0
#             print("option1")
#             while str(follow_buttons[i].text) == "팔로우":
#                 verified_txt = str(recommendation_div.find_elements_by_tag_name('span')[0].text)
#                 print(verified_txt)
#                 if verified_txt == "인증됨" or verified_txt == '':
#                     ignore_button = recommendation_div.find_elements_by_tag_name('button')[0]
#                     ignore_button.click()
#                     break
#                 threshhold+=1;
#                 actions = webdriver.ActionChains(driver)
#                 actions.move_to_element(follow_buttons[i]).click().perform()
#                 time.sleep(1)
#                 if threshhold > 4:
#                     time.sleep(120)
#     except ElementClickInterceptedException:
#         print("!")
#         driver.implicitly_wait(1)
#     except NoSuchElementException:
#
#         driver.implicitly_wait(1)
#         driver.refresh()
#         print("no such elementException")
#         print("!")
#     except StaleElementReferenceException:
#         driver.implicitly_wait(1)
#         print('staleElemenetReferenceException')
#         driver.refresh()
#     except Exception as e:
#         driver.implicitly_wait(1)
#         print("Unexpected error!")
#         print(e.__class__.__name__)

# def follow_influencers_by_recommendation(driver: webdriver):
#     try:
#         recommendation_div = driver.find_element_by_xpath \
#             ('//*[@id="react-root"]/section/main/section/div/div[3]/div/div/div[2]/div/div')
#         follow_buttons = recommendation_div.find_elements_by_tag_name('button')
#         for i in range(len(follow_buttons)):
#             threshhold = 0
#             print("option0")
#             while str(follow_buttons[i].text) == "팔로우":
#                 verified_txt = str(recommendation_div.find_elements_by_tag_name('span')[0].text)
#                 print(verified_txt)
#                 if verified_txt == "인증됨" or verified_txt == '':
#                     ignore_button = recommendation_div.find_elements_by_tag_name('button')[0]
#                     ignore_button.click()
#                     break
#                 threshhold += 1;
#                 actions = webdriver.ActionChains(driver)
#                 actions.move_to_element(follow_buttons[i]).click().perform()
#                 if threshhold > 4:
#                     time.sleep(120)
#                 time.sleep(1)
#     except ElementClickInterceptedException:
#         print("!")
#         driver.implicitly_wait(1)
#     except NoSuchElementException:
#         driver.implicitly_wait(1)
#         follow_influencers_by_recomendation_option1(driver)
#         print("no such elementException")
#         print("!")
#     except StaleElementReferenceException:
#         driver.implicitly_wait(1)
#         print('staleElemenetReferenceException')
#         driver.refresh()
#     except Exception as e:
#         driver.implicitly_wait(1)
#         print("Unexpected error!")
#         print(e.__class__.__name__)



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
    capture_and_parser = None

    def __init__(self):
        self.options = Options()
        self.options.add_argument('--start-fullscreen')  # 전체화면(f11 적용)
        self.capture_and_parser = CapturingAndParsing.CapturingAndParsing()

    def run(self):
        self.driver = webdriver.Chrome('./chromedriver_win32/chromedriver_87.exe')
        self.driver.implicitly_wait(2)
        self.driver.set_window_size(632, 1040)
        self.driver.get('https://www.instagram.com/')
        assert "Instagram" in self.driver.title
        auto_login(self.driver)
        self.capture_and_parser.run(self.driver)
        # epoch = 125
        # for i in range(epoch):
        #     follow_influencers_by_recommendation(self.driver)





