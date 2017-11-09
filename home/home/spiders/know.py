# -*- coding: utf-8 -*-
import scrapy


class KnowSpider(scrapy.Spider):
    name = 'know'
    allowed_domains = ['know.baidu.com']
    start_urls = ['http://know.baidu.com/wenda/question/info?qid=4439920de229e853738f05768f67cd3af4e9aeb&abcdcba']

    def parse(self, response):
        print response.url
        pass
