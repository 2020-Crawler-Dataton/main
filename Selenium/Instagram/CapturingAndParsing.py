from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import numpy as np
import cv2

def driver_exist(driver:webdriver):
    if driver is None:
        return False
    else:
        True

def img_crop(src):
    if src == None:
        return False
    one = None
    two = None
    dst = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    row = int(np.size(dst, axis=0) * 0.3)
    start = dst[0][0]
    col = 0
    condition = True
    while (condition):
        if dst[row][col] > start * 2:
            one = col
            condition = False
        col += 1
    col = np.size(dst, axis=1) - int(one * 0.5)
    condition = True
    while (condition):
        if dst[row][col] > start * 2:
            two = col
            condition = False
        col -= 1
    print(one,two)
    dst = dst[:, one:two + 1]
    condition = True
    row = 0
    cut = None
    while (condition):
        if dst[row][0] > start:
            cut = row
            condition = False
        row += 1
    dst = dst[cut:np.size(dst, axis=0) - 1 - cut, :]
    print(cut)
    return dst
def img_crop_by_fixed_value(src):
    if src == None:
        return False
    dst = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    dst = dst[:, 54:545]
    dst = dst[18:np.size(dst, axis=0) - 19, :]
    return dst
class CapturingAndParsing:
    driver = None

    def __init__(self):
        print("!")

    def set_driver(self, driver: webdriver):
        self.driver = driver

    def entering_story(self, i: int):
        try:
            if driver_exist:
                target_xpath = '//*[@id="react-root"]/section/main/section/div[1]/div[1]/div/div/div/div/ul/' \
                               'li[' + str(i) + ']/div/button'
                self.driver.find_element_by_xpath \
                    (target_xpath).click()
                time.sleep(1)
                if str(self.driver.title) != "스토리 • Instagram":
                    self.driver.back()
                    time.sleep(0.3)
                    self.entering_story(int(i) + 1)
        except:
            return False


    def capture_current_screen(self):
        try:
            id = self.driver.find_element_by_xpath \
                ('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/div/a').text
            time = str(self.driver.find_element_by_xpath \
                           (
                               '//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time').get_attribute(
                "datetime"))
            time = time.replace(":", "_")
            time = time.replace(".", "_")
            dst = "./img/" + str(id) + "`" + str(time) + ".png"
            self.driver.save_screenshot(dst)
            cv2.imwrite(dst, img_crop_by_fixed_value(dst))
        except:
            return False


    def next_story(self):
        condition = None
        try:
            story_section = self.driver.find_element_by_xpath \
                ("""//*[@id="react-root"]/section/div[1]/div/section""")

            #button = story_section.find_elements_by_tag_name('button')
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
        for i in range(2):
            self.set_driver(driver)
            self.entering_story(3)
            self.capturing_sequence()
