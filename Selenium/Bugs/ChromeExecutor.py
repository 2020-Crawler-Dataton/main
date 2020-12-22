# Copyright (C) 2020-2021 github.com/can019
# Author: Gi Deok Park
# Contact: email-park04181@gmail.com

""" ---------------------------- import settings ----------------------------"""
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" ------------------------------------------------------------------------"""

""" ------------------------------ Method area ------------------------------"""


def data_to_csv(data, style_name, option):
    song_df = pd.DataFrame([x for x in data])
    song_df.columns = ['Title', 'Artist', 'Image']

    song_df.drop_duplicates(['Title', 'Artist'], keep='first', inplace=True)

    style_name = style_name.replace("/", "_")

    song_df.to_excel("./data/" + option + "/" + style_name + ".xlsx")


def select_song(driver: webdriver, title_list, artist_list, image_list):
    url = driver.current_url
    request = requests.get(url)
    html = request.text
    bs = BeautifulSoup(html, 'html.parser')

    titles = bs.select('p.title')
    artists = bs.select('p.artist')
    images = bs.select('a.thumbnail')

    for i in range(len(titles)):
        if '[권리없는 곡]' in str(titles[i].text):
            continue
        title = titles[i].text.strip().split('\n')[0]

        anchor_list = artists[i].find_all('a')
        if len(anchor_list) > 1:
            attr = anchor_list[1]['onclick']
            attr = attr.split("'")
            attr = attr[1]
            attr = attr.split("||")

            for word in attr:
                if word.isdigit():
                    attr.remove(word)

            artist = attr[1::2]
            artist = ", ".join(artist)
        else:
            artist = artists[i].text.strip().split('\n')[0]

        image = images[i].find('img')['src']

        title_list.append(title)
        artist_list.append(artist)
        image_list.append(image)

    driver.back()


def select_playlist(driver: webdriver, title_list, artist_list, image_list):
    time.sleep(3)

    for i in range(12):
        playlists = driver.find_elements_by_xpath('//*[@id="container"]/section/div/ul/li')
        playlists[i].click()
        select_song(driver, title_list, artist_list, image_list)
        time.sleep(3)

    driver.back()


def select_style(driver: webdriver):
    styles = driver.find_elements_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[1]/ul/li')
    max_iter = len(styles)

    for i in range(max_iter):
        styles = driver.find_elements_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[1]/ul/li')
        style_name = str(styles[i].text)
        styles[i].find_element_by_tag_name('a').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="container"]/section/div/header/p[2]/a[1]').click()

        title_list = []
        artist_list = []
        image_list = []

        select_playlist(driver, title_list, artist_list, image_list)

        data = zip(title_list, artist_list, image_list)
        data_to_csv(data, style_name, "style")


def select_genre(driver: webdriver):
    genres = driver.find_elements_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[5]/ul/li')
    max_iter = len(genres)

    for i in range(max_iter):
        genres = driver.find_elements_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[5]/ul/li')
        genre_name = str(genres[i].text)
        genres[i].find_element_by_tag_name('a').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="container"]/section/div/header/p[2]/a[1]').click()

        title_list = []
        artist_list = []
        image_list = []

        select_playlist(driver, title_list, artist_list, image_list)

        data = zip(title_list, artist_list, image_list)
        data_to_csv(data, genre_name, "genre")


""" --------------------------------------------------------------------------"""

"""
Class ChromeExecutor.
description: ChormeExecutor acutally acts as a controller.
             If run() ends, program would expire.
"""


class ChromeExecutor:
    options = None
    driver = None
    capture = None
    wait = None

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('lang=ko_KR')  # 언어 설정
        self.options = webdriver.ChromeOptions()

    def run(self):
        self.driver = webdriver.Chrome('./chromedriver_win32/chromedriver_87.exe')
        self.driver.implicitly_wait(2)
        self.driver.get('https://music.bugs.co.kr/musicpd')
        select_style(self.driver)
        select_genre(self.driver)
        self.driver.quit()
