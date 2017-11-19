# -*- coding: utf-8 -*-
import scrapy


class KnowSpider(scrapy.Spider):
    name = 'know'
    allowed_domains = ['know.baidu.com']
    start_urls = ['http://know.baidu.com']

    def parse(self, response):
        print response.url
        print response.url
        print response.url
        print response.url
        pass
