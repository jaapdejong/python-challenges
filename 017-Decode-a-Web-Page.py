#!/usr/bin/python3
#
# Exercise 17 (and Solution)
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
#

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nytimes.com")
text = BeautifulSoup(r.text, "html.parser")
print(text.prettify())

# TODO 
# TODO
