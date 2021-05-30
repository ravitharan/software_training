#! /usr/bin/env python3

import sys
import re
import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload

# Documentation in https://selenium-python.readthedocs.io/

url = 'https://www.daraz.lk/catalog/?_keyori=ss&from=input&page={}&q=usb%20drive&spm=a2a0e.searchlist.search.go.40551ac2OJpGQk'
product_class = "c16H9d"
price_class = "c3gUW0"

price_range = {"min":10, "max":8000}
size_range = {"min":64, "max":8000}
usb_speed_range = {"min":1, "max":1}

size_re = re.compile('\d+\s*[GT]B', re.IGNORECASE)
usb3_re = re.compile('usb\s+3', re.IGNORECASE)
price_re = re.compile('[\d,]+')

# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def upload_file(file_name):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': file_name,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(file_name,
                            mimetype='text/csv',
                            resumable=True)
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='webViewLink').execute()
    print('File link: {}'.format(file.get('webViewLink')))
def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s

def extract_drive_parameters(usb_description):
    size = 0
    usb_3 = 0
    match = size_re.search(usb_description)
    if match:
        value = match.group()
        size = int(value[:-2])
        if value[-2].upper() == 'T': #size in TB
            size *=1000
    match = usb3_re.search(usb_description)
    if match:
        usb_3 = 1
    return (size, usb_3)

def extract_price(usb_price):
    price = 0
    match = price_re.search(usb_price)
    if match:
        value = match.group()
        price = int(value.replace(',', ''))
    return price

def extract_an_item(description, item_price, href):
    (size, usb_3) = extract_drive_parameters(description)
    price = extract_price(item_price)
    if size >= size_range["min"] and size <= size_range[
            "max"] and usb_3 >= usb_speed_range["min"] and usb_3 <= usb_speed_range[
                "max"] and price >= price_range[
                    "min"] and price <= price_range["max"]:
        usb_drive = {}
        usb_drive["size"] = size
        usb_drive["usb3"] = usb_3
        usb_drive["price"] = price
        usb_drive["text"] = description
        usb_drive["link"] = href
        return usb_drive
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Argument error\nUsage: {} [num_pages|item_file]".format(sys.argv[0]))
        exit(1)

    pages = tryint(sys.argv[1])

    items1 = []


    if isinstance(pages, int): # Get from web page
        file_name = f'daraz_usb_{time.strftime("%d_%b_%H_%M")}'
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options, executable_path="/opt/tools/firefox/geckodriver")

        with open(f'{file_name}.txt', mode='w') as out_txt_file:
            for page in range(1,pages+1):
                browser.get(url.format(page))
                products = browser.find_elements_by_class_name(product_class)
                prices = browser.find_elements_by_class_name(price_class)
                for i in range(len(products)):
                    a_tags = products[i].find_elements_by_css_selector("*")
                    href = a_tags[0].get_attribute("href")
                    description = products[i].text
                    item_price = prices[i].text
                    usb_drive = extract_an_item(description, item_price, href)
                    if usb_drive:
                        items1.append(usb_drive)
                    print(products[i].text, prices[i].text)
                    out_txt_file.write(f"{description}`{item_price}`{href}\n")

        browser.quit()
    else: # Get from file
        file_name = os.path.splitext(pages)[0]
        with open(f'{file_name}.txt', mode='r') as in_txt_file:
            for line in in_txt_file:
                [description, item_price, href] = line.rstrip().split('`')
                usb_drive = extract_an_item(description, item_price, href)
                if usb_drive:
                    items1.append(usb_drive)


    items = sorted(items1, key=lambda item: (-item["size"], -item["usb3"], item["price"]))

    with open(f'{file_name}.csv', mode='w') as csv_file:
        fieldnames = ['size', 'usb3', 'price', 'text', 'link']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for item in items:
            writer.writerow(item)

    #print(f"\nUploading {file_name}.csv to google drive...")
    #upload_file(f'{file_name}.csv')
