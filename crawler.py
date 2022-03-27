from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



import pyperclip as pc 
from bs4 import BeautifulSoup
import urllib.request
import requests
import platform
import time
import re
import _thread
import threading
import time
import os
import os.path
from pathlib import Path
import json
from datetime import datetime
import hashlib


class InternetScouting():
    def __init__(self):
        print("Initialize internet crawler ...")
        self.driver = None
        self.initialize_driver()
        
    def initialize_driver(self):
        try:
            options = Options()
            #  Code to disable notifications pop up of Firefox Browser
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_argument("--mute-audio")
          
            try:
                platform_ = platform.system().lower()
                if platform_ in ['linux', 'darwin']:
                    self.driver = webdriver.Firefox(options=options,executable_path="./driver/geckodriver")  # executable_path="./driver/geckodriver",
                else:
                    self.driver = webdriver.Firefox(options=options,
                                                    executable_path='./driver/geckodriver.exe')  # executable_path="./driver/geckodriver.exe",
            except Exception as ex:
                print("Khởi tạo Crawler lỗi", ex)
                self.driver.close()
                return

            self.driver.maximize_window()
            self.driver.get("https://www.google.com/")
            print("Initialize successful!")
        except Exception as e:
            print("Khởi tạo và đăng nhập crawler lỗi", e)

    def reset(self):
        self.request_count += 1
        if self.request_count == 20:
            self.driver.close()
            self.initialize_driver()
            self.request_count = 0

    def request_craw(self):
        # vòng for run các bộ data rộng 10000 dòng 
        for i in range (0,50000,10000):
            # truy cập link
            url = "https://cuongpafat-herokuapp-com.translate.goog/part" +str(i) +".html?_x_tr_sch=http&_x_tr_sl=vi&_x_tr_tl=lo&_x_tr_hl=vi&_x_tr_pto=wapp"
            self.driver.get(url)
            print('waiting')
            time.sleep(120)

            # Cuộn trang web
            print("start scroll")
            SCROLL_PAUSE_TIME = 1.5 
            # Get scroll height
            last_height = self.driver.execute_script("return document.body.scrollHeight")   # Đô dài trang web
            print("len = "+ str(last_height))
            scroll_length = 500
            while True:
                if scroll_length % 10000 == 0 :
                    print("...."+str(scroll_length)+"=>")
                temp = "window.scrollTo(0, " + str(scroll_length) + ");"
                self.driver.execute_script(temp)
                time.sleep(SCROLL_PAUSE_TIME)
                scroll_length += 500
                if scroll_length >= last_height :
                    break 
            print("end scroll.")
            time.sleep(20)
            # Ghi vao file
            print("start write")
            elements = self.driver.find_elements_by_class_name("cuong")
            storyTitles = [el.text for el in elements]
            path = "./result/result_document/result_data_" + str(i) + ".txt"
            f1 = open(path, 'w', encoding='utf-8')
            x = storyTitles[0]
            y = x.split('\\n')
            for i in y :
                f1.write(i + "\n")
                f1.truncate()
if __name__ == "__main__":
    ac = InternetScouting()
    ac.request_craw()







