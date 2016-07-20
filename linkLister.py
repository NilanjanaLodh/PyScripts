import requests
import re
from bs4 import BeautifulSoup
url = raw_input("Enter URL with http or https prefix : " )
website= requests.get(url)
html = website.text

soup = BeautifulSoup(html)
all_links=soup.find_all("a")

for link in all_links:
    print link.get("href")


