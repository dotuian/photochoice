# -*- coding:utf8 -*-
import codecs
import os
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

def parse(filename):
    list = []

    file = open(filename, 'r',encoding="utf8")
    content = file.read()
    file.close()

    soup = BeautifulSoup(content, "html.parser")
    for link in soup.find_all('img'):
        imageLink = link.get('src')
        pattern = re.compile(r"w1_(.+?)/")
        key = re.findall(pattern, imageLink)

        file_name = key[0]
        url = "http://image3.photochoice.net/r/tn_{0}/pc_watermark_6_h/0/".replace("{0}", file_name)
        list.append(url)

    return list

if __name__ == '__main__':
    input="./input"
    filenames = [os.path.join(input, f) for f in os.listdir(input) if os.path.isfile(os.path.join(input, f)) and os.path.splitext(f)[1] == ".txt"]

    print(filenames)
    #
    for filename in filenames:
        urllist = parse(filename)

        output = "output/" + os.path.splitext(os.path.basename(filename))[0]
        print("output: %s" %output)
        if not os.path.exists(output):
            os.makedirs(output)

        count=0
        for url in urllist:
            count = count + 1
            print("[{}／{}] {}".format(count, len(urllist), url))
            download(url, "%s/%s.jpg" %(output, count))
