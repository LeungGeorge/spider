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


class Yh31Spider(scrapy.Spider):
    name = 'yh31'
    allowed_domains = ['qq.yh31.com']
    start_urls = []
    baseDir = '/Users/liangyuanzheng/Documents/workspace/spider/demo/crawl_data' + '/' + name

    def __init__(self, **kwargs):
        print '__init__'
        for pageNum in range(1, 152, 1):
            self.start_urls.append('http://qq.yh31.com/ka/zr/List_' + str(pageNum) + '.html')

        if not os.path.exists(self.baseDir):
            os.makedirs(self.baseDir)

    def parse(self, response):
        print response.url
        page = response.xpath('//*[@id="main_bblm"]/div[1]')
        lis = page.xpath('.//li')

        for sli in lis:
            img = sli.xpath('dt/a/img')
            if img:
                src = sli.xpath('dt/a/img/@src').extract()[0]
                saveUrl = 'http://qq.yh31.com' + src
                saveUrl = saveUrl.replace('http://qq.yh31.comhttp://www.yh31.com', 'http://www.yh31.com')
                print saveUrl

                fileName = hashlib.md5(saveUrl).hexdigest()
                print fileName

                fullFileName = self.baseDir  + '/' +  fileName + '.html'
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