import re
from lxml.html import parse
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url = "https://en.wikipedia.org/wiki/Comparison_of_instruction_set_architectures"
f = Request(url)
page = urlopen(f)

so = BeautifulSoup(page, "lxml")

links = []

for link in so.findAll('a'):
    links.append(link.get('href'))

