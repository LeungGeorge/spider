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

class ZbjuranSpider(scrapy.Spider):
    name = 'zbjuran'
    allowed_domains = ['www.zbjuran.com']
    start_urls = []
    sourceName = 'zbjuran'
    baseDir = './crawl_data/zbjuran/'

    def __init__(self):
        pageNum = 1

        ## 2393
        for pageNum in range(1, 2393, 1):
            url = 'http://www.zbjuran.com/dongtai/list_4_' + str(pageNum) + '.html'
            self.start_urls.append(url)

    def parse(self, response):
        print response.url

        page = response.xpath('/html/body/div[4]/div/div')
        for itm in page:
            try:
                className = itm.xpath('@class').extract()[0]
                if 'item' == className:
                    img = itm.xpath('div/p/img').extract()
                    if img:
                        imgUrl = itm.xpath('div/p/img/@src').extract()[0]
                        saveUrl = 'http://img.zbjuran.com' + imgUrl
                        print saveUrl

                        fileName = hashlib.md5(saveUrl).hexdigest()
                        print fileName

                        fullFileName = self.baseDir + fileName + '.html'
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

                        try:
                            morePage = itm.xpath('div[2]/a').extract()
                            #saveUrl = 'http://img.zbjuran.com' + imgUrl
                            print 'xxxxxxxxxxxxxx'
                            if morePage:
                                morePageUrl = itm.xpath('div[2]/a/@href').extract()[0]
                                urlLen = len(morePageUrl) - len('.html')
                                fullMorePageUrl = 'http://www.zbjuran.com' + morePageUrl[0:urlLen] + "_2.html"
                                print morePageUrl
                                #print fullMorePageUrl
                                for pp in range(2, 6, 1):
                                    fullMorePageUrl = 'http://www.zbjuran.com' + morePageUrl[0:urlLen] + "_" + str(pp) + ".html" + "\n"
                                    print fullMorePageUrl
                                    fileNameLater = './crawl_data/laterCrawler.txt'
                                    fileHandle = open(fileNameLater, 'a')
                                    fileHandle.write(fullMorePageUrl)
                                    fileHandle.close()


                            pass
                        except:
                            pass
            except:
                pass

        def save_my_request(self, response):
            print 'xxxxxxx8888888888'
            print response.url

