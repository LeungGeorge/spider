# -*- coding: utf-8 -*-
import os
import sys
import scrapy
from time import sleep
import random
import json
import hashlib

from crawlfunny.items import CrawlfunnyItem

reload(sys)
sys.setdefaultencoding("utf-8")


class A4399pkSpider(scrapy.Spider):
    name = '4399pk'
    allowed_domains = ['joke.4399pk.com']
    start_urls = []
    baseDir = './crawl_data' + '/' + name

    def __init__(self):
        for pageNum in range(1, 21, 1):
            url = 'http://joke.4399pk.com/funnyimg/find-cate-2-p-' + str(pageNum) + '.html'
            self.start_urls.append(url)
        for pageNum in range(1, 14, 1):
            url = 'http://joke.4399pk.com/funnyimg/find-cate-9-p-' + str(pageNum) + '.html'
            self.start_urls.append(url)

        #self.start_urls.append('http://joke.4399pk.com/funnyimg/find-cate-9-p-1.html')
        #self.start_urls.append('http://joke.4399pk.com/funnyimg/16465.html')

        if not os.path.exists(self.baseDir):
            os.mkdir(self.baseDir)

    def parse(self, response):
        print response.url

        page = response.xpath('/html/body/div[6]/div[1]/ul/li')

        for sli in page:
            htmlUrl = sli.xpath('a/@href').extract()[0]
            print htmlUrl
            yield scrapy.Request(htmlUrl, callback=self.parse_myrequest, )

    def parse_myrequest(self, response):
        page = response.xpath('//*[@id="thumb-ul"]/li')

        for sli in page:
            img = sli.xpath('a/img')
            if img:
                saveUrl = sli.xpath('a/img/@big_src').extract()[0]
                print saveUrl

                fileName = hashlib.md5(saveUrl).hexdigest()
                print fileName

                fullFileName = self.baseDir + '/' + fileName + '.html'
                print fullFileName
                if os.path.isfile(fullFileName):
                    print "file has been created";
                    pass
                else:
                    fileHandle = open(fullFileName, 'w')
                    arrItem2Save = {
                        "source": self.name,
                        "img_original_url": saveUrl,
                    }
                    content = json.dumps(arrItem2Save, ensure_ascii=False)
                    fileHandle.write(content + "\n")
                    fileHandle.close()


