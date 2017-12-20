# -*- coding: utf-8 -*-
import os
import sys
import scrapy
from time import sleep
import random
import json
import hashlib

reload(sys)
sys.setdefaultencoding("utf-8")


class Zbjuran2Spider(scrapy.Spider):
    name = 'zbjuran2'
    allowed_domains = ['www.zbjuran.com']
    start_urls = []
    sourceName = 'zbjuran'
    baseDir = './crawl_data/zbjuran/'

    def __init__(self):
        file = open("./crawl_data/laterCrawler.txt")

        while 1:
            line = file.readline()
            if not line:
                break
            newLine = line.strip()
            print newLine
            print newLine
            print newLine
            self.start_urls.append(newLine)


    def parse(self, response):
        print response.url
        #/html/body/div[5]/div[1]/div[1]/div[2]/p/img
        img = response.xpath('/html/body/div[4]/div/div/div[2]/p/img')
        if img:
            imgUrl = img.xpath('@src').extract()[0]
            print imgUrl
            saveUrl = 'http://img.zbjuran.com' + imgUrl
            print saveUrl

            fileName = hashlib.md5(saveUrl).hexdigest()
            fullFileName = self.baseDir + fileName + '.html'
            print fullFileName
            if os.path.isfile(fullFileName):
                print "file has been created";
                pass
            else:
                fileHandle = open(fullFileName, 'w')
                arrItem2Save = {
                    "source": self.sourceName,
                    "img_original_url": saveUrl,
                }
                content = json.dumps(arrItem2Save, ensure_ascii=False)
                fileHandle.write(content + "\n")
                fileHandle.close()




