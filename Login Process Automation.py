# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:07:18 2023

@author: BISWAJIT
"""

### Login Automation
""" This code is an automation of login process in Hackerrak"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
    driver.get("https://www.hackerrank.com/auth/login")
    return driver


def main():
    driver = get_driver()
    driver.find_element(by="id", value = "input-1").send_keys("user_name")
    time.sleep(2)
    driver.find_element(by="id",value = "input-2").send_keys("password" + Keys.RETURN)
    time.sleep(2)
    
    # Go to the Profile Dropdown
    driver.find_element(by="xpath", value = "/html/body/div[4]/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[5]/div/div[1]/i").click()
    
    driver.find_element(by="xpath",  value = "/html/body/div[4]/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[5]/div/div[2]/ul/li[2]").click()
    print(driver.current_url)
    time.sleep(2)
    #Fetch the Profile Bio
    element = driver.find_element(by = "xpath", value = "//html/body/div[4]/div/div/div/div/div[3]/article/div/div[1]/div/p[2]")
    
    print(driver.current_url)
    print(element.text)
    
    
print(main())
