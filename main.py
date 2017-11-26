# -*- coding:utf8 -*-
import codecs
from bs4 import BeautifulSoup
from requests import get
import re

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)


path = "input/list.txt"
file = open(path,'r',encoding="utf8")
content = file.read()
file.close()

print(content)

soup = BeautifulSoup(content)

for link in soup.find_all('img'):
    imageLink = link.get('src')
    print(imageLink)

    pattern = re.compile(r"w1_(.+?)/")
    key = re.findall(pattern, imageLink)

    file_name = key[0]
    print(file_name)
    url = "http://image3.photochoice.net/r/tn_{0}/pc_watermark_6_h/0/".replace("{0}", file_name)
    print(url)
    download(url, "output/06むしさん　み～つけた/%s.jpg" %file_name)























