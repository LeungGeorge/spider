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


class LaifudaoSpider(scrapy.Spider):
    name = 'laifudao'
    allowed_domains = ['www.laifudao.com']
    start_urls = []
    baseDir = './crawl_data' + '/' + name

    def __init__(self):
        for pageNum in range(1, 691, 1):
            self.start_urls.append('http://www.laifudao.com/tupian/gaoxiaogif_' + str(pageNum) + '.htm')

        if not os.path.exists(self.baseDir):
            os.mkdir(self.baseDir)


    def parse(self, response):
        print response.url
        page = response.xpath('/html/body/div[1]/div/div/section/article')

        for sarticle in page:
            img = sarticle.xpath('div/section/a/img')
            if img:
                try:
                    saveUrl = sarticle.xpath('div/section/a/img/@data-gif').extract()[0]
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
                except:
                    try:
                        saveUrl = sarticle.xpath('div/section/a/img/@src').extract()[0]
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
                    except:
                        pass




