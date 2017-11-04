# -*- coding: utf-8 -*-
import scrapy

from stackoverflow.items import StackoverflowItem

class QuestionSpiderSpider(scrapy.Spider):
    name = 'question_spider'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?page=1&sort=votes']

    def parse(self, response):
        #filename = response.url.split('/')[-2].split('?')[-2] + ".html"
        #with open(filename, 'wb') as fp:
            #fp.write(response.body);

        self.logger.info('hhhhhhhhhhhh', response.url)
        ques = response.xpath('//*[@id="questions"]/div')
        for q in ques:
            item = StackoverflowItem()
            item['title'] = q.xpath('div[2]/h3/a/text()').extract()
            item['votes'] = q.xpath('div[1]/div[2]/div[1]/div[1]/span[1]/strong[1]/text()').extract()
            item['answers'] = q.xpath('div[1]/div[2]/div[2]/strong[1]/text()').extract()
            item['link'] = response.urljoin(q.xpath('div[2]/h3/a/@href').extract()[0])
            item['desc'] = q.xpath('div[2]/div/text()').extract()
            yield item

        page = response.xpath('//*[@id="mainbar"]/div[4]/a')
        for p in page:
            pageTips = p.xpath('span/text()').extract()
            pageTipsStrip = pageTips[0].strip()
            print pageTipsStrip
                                    
            if 'next' == pageTipsStrip:
                nextPageUrl = p.xpath('@href').extract()[0];
                nextPageUrlFull = response.urljoin(nextPageUrl)
                print nextPageUrlFull
                #recurse crawl all page
                #yield scrapy.Request(nextPageUrlFull, callback=self.parse)

