import redis
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider

class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(MyCrawler, self).__init__(*args, **kwargs)
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        self.start_urls.append('http://joke.4399pk.com/funnyimg/find-cate-2.html')

        r = redis.Redis()
        for pageNum in range(1, 20, 1):
            pageUrl = 'http://joke.4399pk.com/funnyimg/find-cate-2-p-' + str(pageNum) + '.html'
            start_urls_len = r.lpush("myspider:start_urls", pageUrl)
            print 'start_urls_len:' + str(start_urls_len)
