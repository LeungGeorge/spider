# -*- coding: utf-8 -*-
import scrapy
import logging

class JianshuspiderSpider(scrapy.Spider):
    name = 'JianShuSpider'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://www.jianshu.com/']
    logger = logging.getLogger('MyLogger')

    def parse(self, response):
        ulList = response.xpath('//ul[@class="note-list"]')
        self.logger.info(ulList)
        print 'content..........'
        #print ulList.extract()
        for li in ulList.xpath('//li'):
        	id = li.xpath('//@id')
        	content = li.xpath('./div[@class="content"]')
        	title = content.xpath('./a[@class="title"]/text()')
        	strTitle = title.extract()
        	abstract = content.xpath('./p[@class="abstract"]/text()')
        	strAbstract = abstract.extract()

        	print "****************"
        	print strTitle
        	print strAbstract


