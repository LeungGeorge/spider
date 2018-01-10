# -*- coding: utf-8 -*-
import os
import sys
import scrapy
import re
from time import sleep
import random
import json
import hashlib
from scrapy.selector import Selector
from scrapy import linkextractors
from scrapy.http import Request,FormRequest
from zhihu.settings import *

reload(sys)
sys.setdefaultencoding("utf-8")

class ZhihuTopicSpider(scrapy.Spider):
    name = 'zhihu_topic'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/topic/19776749/organize/entire']
    baseDir = './crawl_data' + '/' + name

    headers = {
        'HOST': 'www.zhihu.com',
        'Referer': 'https://www.zhihu.com',
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    }

    def __init__(self, **kwargs):
        super(ZhihuTopicSpider, self).__init__(**kwargs)

        if not os.path.exists(self.baseDir):
            os.mkdir(self.baseDir)

    def parse(self, response):
        print 'function_parse'
        print response.url
        print response.text
        pass

    def parse_detail(self, response):
        print 'function_parse_detail'
        # 爬取文章细节
        pass

    # scrapy开始时先进入start_requests()
    def start_requests(self):
        print 'function_start_requests'
        # 为了提取_xsrf：要先访问知乎的登录页面，让scrapy在登录页面获取服务器给我们的数据(_xsrf)，再调用login
        return [scrapy.Request('https://www.zhihu.com/#signin', headers=self.headers, callback=self.login)]

    def login(self, response):
        print 'function_login'
        xsrf = '37663530313565642d646666642d346361312d613930392d653464656439373238353762'
        match_obj = re.match('[\s\S]*name="_xsrf" value="(.*?)"', response.text)
        if match_obj:
            #xsrf = match_obj.group(1)
            pass
        # 如果提取到了xsrf就进行下面的操作，如果没xsrf有就没必要往下做了
        if xsrf:
            post_data = {
                'captcha_type': 'cn',
                '_xsrf': xsrf,
                #'phone_num': '13043330319',
                'phone_num': '13070160573',
                #'password': 'Wcw19961223',
                'password': 'lyzhyw5173',
                'captcha': '',
            }
            import time
            captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (int(time.time() * 1000))
            # scrapy会默认把Request的cookie放进去
            return scrapy.Request(captcha_url, headers=self.headers, meta={'post_data': post_data},
                                  callback=self.login_after_captcha)

    def login_after_captcha(self, response):
        # 保存并打开验证码
        print 'function_login_after_captcha'
        with open('captcha.gif', 'wb') as f:
            f.write(response.body)
            f.close()
        from PIL import Image
        try:
            img = Image.open('captcha.gif')
            img.show()
        except:
            pass
        # 输入验证码
        captcha = {
            'img_size': [200, 44],
            'input_points': [],
        }
        points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20],
                  [129.796875, 22], [150.796875, 22]]
        seq = input('请输入倒立字的位置\n>')
        for i in seq:
            captcha['input_points'].append(points[int(i) - 1])
        captcha = json.dumps(captcha)

        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = response.meta.get('post_data', {})
        post_data['captcha'] = captcha
        return [scrapy.FormRequest(
            # 在这里完成像之前的requests的登录操作，每一个Request如果要做下一步处理都要设置callback
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login,
        )]

    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功
        text_json = json.loads(response.text)
        print text_json
        if 'msg' in text_json and text_json['msg'] == '登录成功':
            print('登录成功！')
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)


