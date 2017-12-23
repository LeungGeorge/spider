from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import redis

class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['joke.4399pk.com']
    start_urls = []

    rules = (
        Rule(LinkExtractor(allow=(r'http://joke.4399pk.com/funnyimg/.+')), callback='parse_item', follow=True),
    )
    #/questions/11227809/why-is-it-faster-to-process-a-sorted-array-than-an-unsorted-array

    def __init__(self,*args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        self.start_urls.append('http://joke.4399pk.com/funnyimg/find-cate-2.html')
        rrr = redis.Redis()

        data = rrr.llen("myspider_redis:items")

        print 'xxxxxxxxxxxxxx777777777'
        print data

    def parse_item(self, response):
        print 'xxxxxxxxxxxxxxxxxxx'
        print response.url