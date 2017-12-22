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

class JokejiSpider(scrapy.Spider):
    name = 'jokeji'
    allowed_domains = ['http://gaoxiao.jokeji.cn']
    start_urls = []

    sourceName = 'jokeji'
    baseDir = './crawl_data/jokeji/'

    def __init__(self, **kwargs):
        super(JokejiSpider, self).__init__(**kwargs)
        pageNum = 1

        ## 2393
        for pageNum in range(1, 2, 1):
            url = 'http://gaoxiao.jokeji.cn/search.asp?MaxPerPage=8&cid=15&keyword=%B6%F1%B8%E3&&me_page=' + str(pageNum)
            self.start_urls.append(url)

    def parse(self, response):
        print response.url


        page = response.xpath('/html/body/div[2]/div[2]/div')

        for itm in page:
            try:
                className = itm.xpath('@class').extract()[0]
                print 'ccccccc'
                print className
                if 'list_list' == className:
                    img = itm.xpath('ul/li/span/a[2]/img').extract()
                    print 'xxxxxxxxx'
                    print img
                    if img:
                        imgUrl = itm.xpath('ul/li/span/a[2]/img/@src').extract()[0]
                        saveUrl = 'http://gaoxiao.jokeji.cn' + imgUrl
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

            except:
                pass

