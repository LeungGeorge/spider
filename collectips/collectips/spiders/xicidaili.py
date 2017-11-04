# -*- coding: utf-8 -*-
import scrapy

from collectips.items import CollectipsItem

class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/1']

    def parse(self, response):
        ip_list = response.xpath('//*[@id="ip_list"]')
        trs = ip_list[0].xpath('tr')

        for tr in trs[1:]:
            item = CollectipsItem()

            item['ip'] = tr.xpath('td[2]/text()').extract()
            item['port'] = tr.xpath('td[3]/text()').extract()
            item['server_address'] = tr.xpath('td[4]/a/text()').extract()
            item['is_gao_ni'] = tr.xpath('td[5]/text()').extract()
            item['ip_type'] = tr.xpath('td[6]/text()').extract()
            item['speed'] = tr.xpath('td[7]/div/@title').extract()[0]
            item['connection_time'] = tr.xpath('td[8]/div/@title').extract()[0]
            item['alive_time'] = tr.xpath('td[9]/text()').extract()
            item['check_time'] = tr.xpath('td[10]/text()').extract()
            yield item

        pagination = response.xpath('//*[@id="body"]/div[2]')
        alist = pagination[0].xpath('a')

        for a in alist:
            class_name = a.xpath('text()').extract()
            class_name2 = class_name[0].strip()
            if u'下一页 ›' == class_name2:
                print 'next page...............'
                nextPageHref = a.xpath('@href').extract()[0]
                nextPageHrefFullUrl = response.urljoin(nextPageHref)
                #yield scrapy.Request(nextPageHrefFullUrl, callback=self.parse)

