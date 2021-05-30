#! /usr/bin/env python3

import sys
import re
import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Documentation in https://selenium-python.readthedocs.io/

url = 'https://www.nasdaq.com/market-activity/stocks'
stock_price_class = "symbol-page-header__pricing-price"

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print(f"Argument error\nUsage: {sys.argv[0]} <company_symbol1> [company_symbol2 company_symbol3 ... ]")
        exit(1)


    companies = sys.argv[1:]

    options = Options()
    options.headless = True

    with webdriver.Firefox(options=options, executable_path="/opt/tools/firefox/geckodriver") as driver:
        for company in companies:
            print(f"{company:<10}", end = '')
        print()
        for i in range(10):
            for company in companies:
                driver.get(f"{url}/{company}")

                for j in range(10):
                    prices = driver.find_elements_by_class_name(stock_price_class)
                    value = prices[1].text
                    if value:
                        break
                    else:
                        time.sleep(1)

                if value:
                    price = float(value[1:])
                    print(f"{price:<10}", end = '')
                else:
                    print(f"{i}: ERROR price is empty")
            print()

