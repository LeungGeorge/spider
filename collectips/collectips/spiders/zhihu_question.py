# -*- coding: utf-8 -*-
import os
import sys
import scrapy
from time import sleep
import random
import json

from collectips.items import CollectipsZhiHuItem

reload(sys)
sys.setdefaultencoding("utf-8")

class ZhihuQuestionSpider(scrapy.Spider):
    name = 'zhihu_question'
    allowed_domains = ['www.zhihu.com']
    start_urls = []

    def __init__(self):
        tmp_start_urls = [
            'http://www.zhihu.com/question/43472837',
        ]
        for uurrll in tmp_start_urls:
            qid = uurrll.split('/')[-1]
            filename = './data/' + str(qid) + '_question.txt'
            print filename
            if os.path.isfile(filename):
                print "file has been created";
            else:
                self.start_urls.append(uurrll)
        for uurrll in self.start_urls:
            print uurrll

        self.headers = {
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding':'gzip, deflate', 
            'Host': 'www.zhihu.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Cookie':'aliyungf_tc=AQAAAMsWXn+qbQoAbia13HCe/HxZwKkc; d_c0="AGBC376spgyPTvos41-IEE_4565HfFlezaY=|1510123785"; q_c1=62973788bb154498bf7051c98e18a4ce|1510123787000|1510123787000; _zap=02ab18c5-05d2-4393-88fb-c4945bf6286c; _xsrf=aabbc999-6d4d-4549-ac97-8506e1e9d33a',
         } 

        self.reply_headers = {
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding':'gzip, deflate', 
            'Host': 'www.zhihu.com',
            'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
            'Cookie': 'aliyungf_tc=AQAAAMsWXn+qbQoAbia13HCe/HxZwKkc; d_c0="AGBC376spgyPTvos41-IEE_4565HfFlezaY=|1510123785"; q_c1=62973788bb154498bf7051c98e18a4ce|1510123787000|1510123787000; _zap=02ab18c5-05d2-4393-88fb-c4945bf6286c; l_cap_id="OTQ1MGRhODllY2E1NDMyOTk3MDZiYzE2ZWQzNzI3OWQ=|1510127157|034fdbb7608c66504bf27b24ad5f5e4c515ddd39"; r_cap_id="OGFmNjk3NjJmZmFkNGJkMjgxYWI0MDg4ZjUzZDcyNzQ=|1510127157|e4f93b11c556ad14fca84d40e84443fdf3dbd792"; cap_id="YmIwOGFmODlmMTQzNDQyMmJmZjgyYzNjYmFmZjdmMjE=|1510127157|4051ff5b7fc5fda2d6998a8062d17c13b0fde966"; _xsrf=aabbc999-6d4d-4549-ac97-8506e1e9d33a',
       }


    def parse(self, response):
        qid = response.url.split('/')[-1]
        filename = './data/' + str(qid) + '_question.txt'
        if os.path.isfile(filename):
            print "file has been created";
            pass
        else:
            print response.url
            file = open(filename, 'wa')

            item = CollectipsZhiHuItem()
            item['url'] = response.url
            item['reply_url'] = response.url

            title = response.xpath('//*[@id="root"]/div/main/div/div[1]/div[1]/div[1]/div[1]/h1/text()').extract()[0]
            question_content = response.xpath('//*[@id="root"]/div/main/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]').extract()[0]

            question_info = {
                'title' : title,
                'content' : question_content,
            }
            strQues = json.dumps(question_info, ensure_ascii=False)
            file.write(strQues)
            file.close()

            print title

            reply_url_full = 'https://www.zhihu.com/api/v4/questions/' + str(qid)+ '/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20&sort_by=default'

            print reply_url_full
            sleep(1)
            yield scrapy.Request(reply_url_full, callback=self.save_reply_list, headers = self.reply_headers)


       # #yield item

    def save_reply_list(self, response):
        jsonResponse = json.loads(response.body_as_unicode())

        qid = response.url.split('/')[6]
        data = jsonResponse['data']
        if data:
            for dt in data:
                rid = dt['id']
                filename = './data/' + str(qid) + '_' + str(rid) + '_reply.txt'
                file = open(filename, 'wa')
                print "save reply info"
                print rid

                question_info = {
                    'qid' : qid,
                    'rid' : rid,
                    'reply_info' : dt,
                }
                strQues = json.dumps(question_info, ensure_ascii=False)
                file.write(strQues)
                file.close()

        is_end = jsonResponse['paging']['is_end']
        if is_end == True:
            pass
        else:
            print "get next page reply info"
            nextPage = jsonResponse['paging']['next']
            print nextPage
            sleep(1)
            yield scrapy.Request(nextPage, callback=self.save_reply_list, headers = self.reply_headers)
            pass




