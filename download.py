# while running this script, first specify the file type, then the url from which to retrieve those files
# EG :
#python  download.py pdf http://www.example.com 
# downloads all pdfs from example.com

import sys
import urllib
import requests
from bs4 import BeautifulSoup
from sys import argv
import re

file_ext = argv[1]
url = argv[2] 
website= requests.get(url)
#print 'retrieved website'
html = website.text

soup = BeautifulSoup(html,"lxml")
all_links=soup.find_all("a")

valid_links=[]
preferredfile_re=re.compile('.*\\.'+file_ext)
absolute_url_re=re.compile('.*://.*')
base_url_re = re.compile('.+://.+/')
base_url = base_url_re.match(url).group()

for link in all_links:
    href= link.get("href")
    if preferredfile_re.search(href) :
        valid_links.append(href)

print len(valid_links) , " files found."
for i,link in enumerate(valid_links):
    if not absolute_url_re.search(link):
        #this means this is a relative url, and we need to make it absolute
        valid_links[i] = base_url + link
    
    valid_links[i]=valid_links[i].replace(" ","%20")#take care of the encoding        
    file_name= link.split('/')[-1]
    print 'Downloading ' , file_name ,' ....  ',
    sys.stdout.flush()
    urllib.urlretrieve(valid_links[i],file_name)
    print 'done!'

