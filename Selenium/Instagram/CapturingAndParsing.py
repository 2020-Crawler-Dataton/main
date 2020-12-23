from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import numpy as np
import cv2


def driver_exist(driver: webdriver):
    if driver is None:
        return False
    else:
        True

def skip_store_login_info(driver: webdriver):
    time.sleep(1)
    try:
        element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        element.click()
        return True
    except Exception as e:
        print(e.__class__.__name__)
        return False

def img_crop_by_fixed_value(src):
    dst = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    dst = dst[:, 54:545]
    dst = dst[68:np.size(dst, axis=0) - 19, :]
    dst = dst[:744, :]
    return dst


class CapturingAndParsing:
    driver = None

    def __init__(self):
        print("!")

    def set_driver(self, driver: webdriver):
        self.driver = driver

    def entering_story(self, i: int):
        if driver_exist:
            try:
                if str(self.driver.title) == "스토리 • Instagram":
                    return True
                skip_store_login_info(self.driver)
                target_xpath = '//*[@id="react-root"]/section/main/section/div[1]/div[1]/div/div/div/div/ul/' \
                           'li['+str(i)+']/div/button'
                self.driver.find_element_by_xpath\
                    (target_xpath).click()
            except:
                skip_store_login_info(self.driver)
                target_xpath = '//*[@id="react-root"]/section/main/section/div/div[1]/div/div/div/div/ul/' \
                               'li['+str(i)+']/div/button'
                self.driver.find_element_by_xpath \
                    (target_xpath).click()
            time.sleep(1)

            if str(self.driver.title) != "스토리 • Instagram":
                self.driver.back()
                time.sleep(0.3)
                self.entering_story(int(i) + 1)

    def capture_current_screen(self):
        try:
            id = self.driver.find_element_by_xpath \
                ('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/div/a').text
            datetime = str(self.driver.find_element_by_xpath \
                           (
                               '//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time').get_attribute(
                "datetime"))
            datetime = datetime.replace(":", "_")
            datetime = datetime.replace(".", "_")
            dst = "./tmp/" + str(id) + "`" + str(datetime) + ".png"
            print(dst)
            self.driver.save_screenshot(dst)
            cv2.imwrite(dst, img_crop_by_fixed_value(dst))
        except Exception as e:
            """
                폭력적인 image가 있는 경우
            """
            time.sleep(3)
            print(e.__class__.__name__)

    def next_story(self):
        condition = None
        try:
            button = self.driver.find_element_by_xpath('// *[ @ id = "react-root"] / section / div[1] / div / section / div / button[2]')
            button.click()
            condition = True
        except NoSuchElementException as e:
            """
                Read all of stories
            """
            condition = False
        finally:
            time.sleep(0.5)
            return condition

    def capturing_sequence(self):
        condition = True
        while(condition):
            self.capture_current_screen()
            time.sleep(0.3)
            condition = self.next_story()
            print(condition)
            time.sleep(0.3)
    def run(self, driver: webdriver):
        for i in range(10):
            self.set_driver(driver)
            self.entering_story(3)
            time.sleep(0.3)
            self.capturing_sequence()





