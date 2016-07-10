import requests
import re

url = raw_input("Enter URL with http or https prefix : " )
print url
website= requests.get(url)

html = website.text
print html
linklist = re.findall('"((http|ftp)s?://.*?)"',html)
print linklist
for link in linklist:
    print link[0]
