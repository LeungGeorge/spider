# -*- coding: utf-8 -*-
import scrapy
import requests
import sys

from collectips.items import CollectipsItem

class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/1']

    def __init__(self):  
        self.headers = {  
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  
            'Accept-Encoding':'gzip, deflate',  
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'  

    } 

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
            myProxy = str(tr.xpath('td[2]/text()').extract()[0]) + str(':') + str(tr.xpath('td[3]/text()').extract()[0])
            if self.is_valid_ip(myProxy) == 1:
                print 'save a valid ip'
                objFile = open('ip_port_list.txt', 'a')
                rowData = myProxy
                objFile.write(rowData)
                objFile.write('\n')
                objFile.close()
                yield item

        pagination = response.xpath('//*[@id="body"]/div[2]')
        alist = pagination[0].xpath('a')
        pageNum = response.url.split('/')[-1]
        if pageNum >= 5:
            print 'crawl end...'
            exit(0)

        for a in alist:
            class_name = a.xpath('text()').extract()
            class_name2 = class_name[0].strip()
            if u'下一页 ›' == class_name2:
                print 'next page...............'
                nextPageHref = a.xpath('@href').extract()[0]
                nextPageHrefFullUrl = response.urljoin(nextPageHref)
                yield scrapy.Request(nextPageHrefFullUrl, callback=self.parse)

    def is_valid_ip(self, proxy):
        print 'check ip...'
        
        try:
            protocol = 'http://'
            proxies = {protocol: proxy}
            if requests.get('http://www.baidu.com', proxies=proxies, timeout=2).status_code == 200:
                return 1
        except:
            print 'ip is not valid...'
            pass 

        return 0
    


