# -*- coding: utf-8 -*-
import scrapy
import logging

from jianshu.items import JianshuItem

class JianshuspiderSpider(scrapy.Spider):
    name = 'JianShuSpider'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://www.jianshu.com/']
    logger = logging.getLogger('MyLogger')

    def parse(self, response):
        ulList = response.xpath('//ul[@class="note-list"]')
        self.logger.info(ulList)
        #print ulList.extract()
        items = []
        for li in ulList.xpath('//li'):
            id = li.xpath('//@id')
            content = li.xpath('./div[@class="content"]')
            title = content.xpath('./a[@class="title"]/text()')
            strTitle = title.extract()
            abstract = content.xpath('./p[@class="abstract"]/text()')
            strAbstract = abstract.extract()

            item = JianshuItem()
            item['title'] = strTitle
            item['abstract'] = strAbstract

            items.append(item)

        return items

