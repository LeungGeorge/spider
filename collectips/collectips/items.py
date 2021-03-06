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

class CollectipsTouTiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ret_content               = scrapy.Field()
    url                       = scrapy.Field()

class CollectipsZhiHuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url                       = scrapy.Field()
    reply_url                  = scrapy.Field()
    title                     = scrapy.Field()
    qid                       = scrapy.Field()
    rid                       = scrapy.Field()
    content                   = scrapy.Field()

