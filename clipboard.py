#!/usr/bin/python
#This script copies the contents of the file to clipboard
#This may be useful during online competitions where 
# you write the code and copy and paste it into the browser
#Read README for instructions on how to use this script

from sys import argv
import pyperclip

filename = argv[1]
fileObj= open(filename)
fileTxt = fileObj.read()

pyperclip.copy(fileTxt)
fileObj.close()

