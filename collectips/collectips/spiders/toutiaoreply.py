# -*- coding: utf-8 -*-

import json
from time import sleep
import random
import scrapy

from collectips.items import CollectipsTouTiaoItem

class ToutiaoreplySpider(scrapy.Spider):
    name = 'toutiaoreply'
    allowed_domains = ['www.wukong.com']
    start_urls = ['https://www.wukong.com/wenda/web/question/loadmorev1/?qid=6420249595023982849&count=10&req_type=1&offset=0']

    def parse(self, response):
        f = open('/Users/liangyuanzheng/Documents/workspace/spider/question_tou_tiao_list.txt')
        line = f.readline()
        rowCT = 0
        while line:
            sleep(1)
            rowCT = rowCT+1
            if 1 < rowCT:
                arrLine = line.strip().split("\t")
                url_full = 'https://www.wukong.com/wenda/web/question/loadmorev1/?count=10&req_type=1&offset=0' + '&qid=' + arrLine[2]
                crawlFlag = 'rowCTTTTTTTTTTTTT:' + str(rowCT)
                print crawlFlag
                print url_full
                yield scrapy.Request(url_full, callback=self.parse_question_reply, )

            line = f.readline()

    def parse_question_reply(self, response):
        item = CollectipsTouTiaoItem()
        jsonResponse = json.loads(response.body_as_unicode())
        item['ret_content'] = jsonResponse
        item['url'] = response.url
        yield item


