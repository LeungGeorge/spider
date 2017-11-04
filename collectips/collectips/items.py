# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CollectipsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip               = scrapy.Field()
    port             = scrapy.Field()
    server_address   = scrapy.Field()
    is_gao_ni        = scrapy.Field()
    ip_type          = scrapy.Field()
    speed            = scrapy.Field()
    connection_time  = scrapy.Field()
    alive_time       = scrapy.Field()
    check_time       = scrapy.Field()

