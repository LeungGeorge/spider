# -*- coding: utf-8 -*-
import os
import sys
import scrapy
from time import sleep
import random
import json
import hashlib

from crawlfunny.items import CrawlfunnyDemo4399PKItem

reload(sys)
sys.setdefaultencoding("utf-8")


class Demo4399pkSpider(scrapy.Spider):
    name = 'demo4399pk'
    allowed_domains = ['joke.4399pk.com']
    start_urls = []

    def __init__(self):
        self.start_urls.append('http://joke.4399pk.com/funnyimg/find-cate-2.html')

    def parse(self, response):
        page = response.xpath('/html/body/div[6]/div[1]/ul/li')

        for sli in page:
            htmlUrl = sli.xpath('a/@href').extract()[0]
            print htmlUrl
            yield scrapy.Request(htmlUrl, callback=self.parse_single_page, )

    def parse_single_page(self, response):
        page = response.xpath('//*[@id="thumb-ul"]/li')

        for sli in page:
            img = sli.xpath('a/img')
            if img:
                saveUrl = sli.xpath('a/img/@big_src').extract()[0]
                print saveUrl

                item = CrawlfunnyDemo4399PKItem()
                item['source'] = self.name
                item['img_original_url'] = saveUrl

                yield  item
