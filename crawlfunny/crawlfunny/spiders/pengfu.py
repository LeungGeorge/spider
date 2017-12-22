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

class PengfuSpider(scrapy.Spider):
    name = 'pengfu'
    allowed_domains = ['www.pengfu.com']
    start_urls = []
    sourceName = 'pengfu'
    baseDir = './crawl_data/pengfu/'

    def __init__(self, **kwargs):
        super(PengfuSpider, self).__init__(**kwargs)
        pageNum = 1

        ## 2393
        for pageNum in range(1, 26, 1):
            url = 'https://www.pengfu.com/qutu_' + str(pageNum) + '.html'
            self.start_urls.append(url)

    def parse(self, response):
        print response.url
        page = response.xpath('/html/body/div/div[1]/div')

        for itm in page:
            try:
                className = itm.xpath('@class').extract()[0]
                if 'list-item bg1 b1 boxshadow' == className:
                    img = itm.xpath('dl/dd/div[2]/img').extract()
                    if img:
                        imgUrl = itm.xpath('dl/dd/div[2]/img/@src').extract()[0]
                        saveUrl = imgUrl
                        print saveUrl

                        fileName = hashlib.md5(saveUrl).hexdigest()
                        print fileName

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
                pass
            except:
                pass
