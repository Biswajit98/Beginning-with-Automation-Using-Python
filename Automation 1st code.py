# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 00:23:56 2023

@author: BISWAJIT
"""

import selenium
from selenium import webdriver
import time
from datetime import datetime as dt
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\BISWAJIT\\Downloads\\chromedriver.exe')


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(service = service, options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver

def only_value(text):
    temperature = float(text.split(": ")[1])
    return temperature
    
def create_file(text):
    """ Creating file to save the data from automation output"""
    filename= f"{dt.now().strftime('%Y-%m-%d,%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    for i in range(5):
        time.sleep(2)
        #element = driver.find_element(by="xpath", value = "/html/body/div[1]/div/h1[1]")
        nxt_element = driver.find_element(by = "xpath", value = '/html/body/div[1]/div/h1[2]')
        text = str(only_value(nxt_element.text))
        create_file(text)
        
    
    #result = element.text, nxt_element.text
    #return result


print(main())










