# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CrawlfunnyDemo4399PKItem(scrapy.Item):
    source = scrapy.Field()
    img_original_url = scrapy.Field()