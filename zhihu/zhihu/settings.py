# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'
#HTTPERROR_ALLOWED_CODES = [200]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
    'zhihu.middlewares.ZhihuSpiderMiddleware': 110,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.ZhihuPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IP_POOL = [
    {"ipaddr":"59.40.69.231:8010"},
    {"ipaddr":"27.219.36.127:8118"},
    {"ipaddr":"118.187.58.34:53281"},
    {"ipaddr":"117.78.37.198:8000"},
    {"ipaddr":"42.55.171.123:80"},
    {"ipaddr":"119.115.21.17:80"},
    {"ipaddr":"17-11-05 11:44:4395"},
    {"ipaddr":"59.40.50.169:8010"},
    {"ipaddr":"61.129.70.131:8080"},
    {"ipaddr":"61.152.81.193:9100"},
    {"ipaddr":"120.204.85.29:3128"},
    {"ipaddr":"219.228.126.86:8123"},
    {"ipaddr":"61.152.81.193:9100"},
    {"ipaddr":"218.82.33.225:53853"},
    {"ipaddr":"223.167.190.17:42789"},
]

USER_AGENT_LIST = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
    "baidu：Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
]

HEADERS = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '_zap=91c5cb4b-f1bd-48c8-bafa-41b9d77c7912; q_c1=f2376b2df70e40fea308625b837769a2|1488276213000|1488276213000; cap_id="MGQ3MTMzNjhiNDY0NGMyNzhlYTBiYjc1NzY1YzNmZGM=|1488276213|cf3ec5364ebfbac50d1e4e6b986c41d1cd12ee56"; l_cap_id="MjA0MDdiMjZlZTRlNDQyMTkxY2RhMjU5NTNjZGEwNTc=|1488276213|5e15383a9cf6c0b5463c82cab91132b291046622"; d_c0="AFBCnt4eYQuPTj30Vr-Xm_QnQquuzjHvmYI=|1488276213"; nweb_qa=heifetz; __utma=51854390.1790662898.1488276234.1488276234.1488276234.1; __utmz=51854390.1488276234.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|2=registration_date=20160926=1^3=entry_date=20170228=1; login="Njk4NjE4M2YyNzA2NDkzYWE2NzgzMjAxYmY5MTU3ZDY=|1488276254|73f8c0dfa3ff3295423d0c22ba4b63ac8acdc7e9"; _xsrf=d7096ea4ba775327da463404cd7ee43b; aliyungf_tc=AQAAAEYwjwl9wAUAcSa13EA1Fr/WVZxU; __utmc=51854390; _zap=66c55a56-a5dc-48db-ab42-af7746cebdd9',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    #'Referer': 'https://www.zhihu.com/topic/19776749/organize/entire',
}

# cookie地址
# https://brantou.github.io/2017/08/22/scrapy-crawl-zhihu/
COOKIES = {
    'd_c0':'"AICgTHHN7wyPTruaLIczFzsPGjrw_IzgEWU=|1515031304"',
    '__utma':'51854390.1007857646.1515031308.1515031308.1515031308.1',
    '__utmv':'51854390.100--|2=registration_date=20160926=1^3=entry_date=20160926=1',
    '_zap':'eddfa77f-db57-471b-83d5-1084596906a6',
    'q_c1':'8336b388dd3147b5964484679c9a5247|1515035018000|1515035018000',
    'aliyungf_tc':'AQAAAJw/wGAz0QYATqmHPVAEfDv9ftTs',
    '_xsrf':'a968b91d-beb5-4a18-a75e-de572388ed1b',
    'l_cap_id':'"OTJjYWY1YWQzZWEwNDE4NzkyNGJjM2FkMWY5YmI5MmU=|1515035018|032de779ce30f75898971c7832bfbb919212fb51"',
    'r_cap_id':'"NWJmOWVhNDdiNTVkNDk1MTg5MWIwNjI3YmFjYjZhMDk=|1515031301|2ace22ab174bee074ad3c3c4c92738bc210cd504"',
    'cap_id':'"ZWE0NjM0ZTNhNDY0NDBiOThiM2RjMmRjZjZjYjBlYmQ=|1515031301|f5ca1295e3ffa0de72b068dbfc0bdecd2c09329c"',
}
