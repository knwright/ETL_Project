from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import csv
from urllib3.request import urlopen

url_list = []
# Open the url file in read mode
with open("urlfile.csv", "r") as csvf:
    urls = csv.reader(csvf)
    for url in urls:
        # Add each url to the url_list
        url_list.append(url)

for url in url_list:
    page = urlopen(url[0]).read()
    soup = BeautifulSoup(page, "html.parser")

print(soup)

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()



    # Return results
    return costa_data
