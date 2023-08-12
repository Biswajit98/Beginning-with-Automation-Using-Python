# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 01:58:56 2023

@author: BISWAJIT
"""


# Scrap Curency with Beutiful Soup

import bs4
from bs4 import BeautifulSoup
import requests



def get_currency(input_currency, conv_currency):
    url = f'https://www.x-rates.com/calculator/?from={input_currency}&to={conv_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency_rate = float(soup.find("span", class_ = "ccOutputRslt").get_text()[:-4])
    
    
    return currency_rate
    
current_rate = get_currency('INR', 'DKK')
print("1 INR is equal to",current_rate,"DKK")



    