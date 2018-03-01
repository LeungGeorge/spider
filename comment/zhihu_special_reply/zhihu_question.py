#!/usr/bin/python
#!coding:utf-8

import os
import ssl
import requests
import urllib2
import urllib
import sys
from bs4 import BeautifulSoup
import time
import re
import json
import traceback
import urllib2
import random
import hashlib

reload(sys)

sys.setdefaultencoding('utf-8')

class CSpider:
    '''spider'''
    baseDir = './crawl_data/'
    baseUrl = 'https://weibo.com'
    #091e9c5e808e80c8
    baseID = '091e9c5e808e'
    # [20672,36035]
    subID = 36035

    #random.choice(srandTime)
    srandTime = [
        1,
    ]

    header_info = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Host': 'www.zhihu.com',
        'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Cookie': 'aliyungf_tc=AQAAAAT3iHOOygYATqmHPVUtV9+D2WXL; d_c0="AFBjPB7z9wyPTnpYux7Ti_grCBWBkzCi9NQ=|1515578051"; _xsrf=d8725da4-970a-4530-a1eb-3960b6fcc13d; q_c1=a785f810b6da458186f6bb9271108960|1515578051000|1515578051000; _zap=267854b7-08e0-492d-adc4-d2b75b35132f'


    }

    def __init__(self):
        print 'init...'
        self.makeDir(self.baseDir)

    def sleepSec(self, seconds):
        print 'sleep...'
        time.sleep(seconds)

    def makeDir(self, dirName):
        print 'makeDir...:' + dirName
        if not os.path.exists(dirName):
            os.makedirs(dirName)

    def saveFile(self, fileName, content):
        print  'saveFile...' + fileName
        fileHandle = open(fileName, 'wb')
        #u1 = content.decode('gb2312')
        fileHandle.write(content)
        fileHandle.close()

    def writeLog(self, content):
        print content
        fileName = time.strftime("%Y%m%d%H", time.localtime())
        fileName = self.baseDir + "logs/" + fileName + ".log"
        if not os.path.exists(self.baseDir + "logs/"):
            os.makedirs(self.baseDir + "logs/")

        fileHandle = open(fileName, 'a')
        fileHandle.write(content + "\n")
        fileHandle.close()

    def getHtml(self, url):
        #print 'getHtml...'
        #html = requests.get(url, verify=False)
        html = requests.get(url)
        print html.content
        return html

    def get_question_page(self, r_url):
        r_content = ''
        try:
            print r_url
            r_content = requests.get(r_url, verify=False, headers=self.header_info).content
            print r_content
            scl_soup = BeautifulSoup(r_content, "html.parser")
            r_content = scl_soup.find('div', {"class": "RichContent-inner"})
            print r_content.content
            return
            if r_content.find('来源链接是否正确') != -1:
                page_res = {}
                page_res['data'] = []
                page_res['paging'] = {};
                page_res['paging']['is_end'] = True;
                return page_res
            # r_content = requests.get(r_url, headers=header_info).content
            r_json = json.loads(r_content)
            if r_json.has_key("error"):
                print r_content
                return None
            return r_json
        except  Exception, e:
            return None


    def get_reply_raw(self, qid, offset, limit):
        r_content = ''
        try:
            r_url = "https://www.zhihu.com/api/v4/questions/" + str(
                qid) + "/answers?sort_by=default&include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics&limit=" + str(
                limit) + "&offset=" + str(offset);

                    #https://www.zhihu.com/api/v4/questions/21933888/answers?sort_by=default&include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics&limit=20&offset=23
            r_content = requests.get(r_url, verify=False, headers=self.header_info).content
            if r_content.find('来源链接是否正确') != -1:
                page_res = {}
                page_res['data'] = []
                page_res['paging'] = {};
                page_res['paging']['is_end'] = True;
                return page_res
            # r_content = requests.get(r_url, headers=header_info).content
            r_json = json.loads(r_content)
            if r_json.has_key("error"):
                print r_content
                return None
            return r_json
        except  Exception, e:
            return None


print 'start...'

obj = CSpider();


file = open('question_list.txt')
arrQuestionList = []
while True:
    line = file.readline()
    if not line:
        break;
    arrLine = line.split('\t')
    arrPV = {
        "title": arrLine[0],
        "url": arrLine[1],
    }
    content = json.dumps(arrPV, ensure_ascii=False)
    arrQuestionList.append(content)

for inputData in arrQuestionList:
    data = json.loads(inputData)
    qid = data[u'url'].split('/')[4].strip();
    data[u'qid'] = qid
    arrReplyList = []
    pageSize = 10
    fileName = obj.baseDir + str(qid) + '.html'
    print fileName
    if os.path.isfile(fileName):
        print 'file has been saved...'
        continue
    for offset in range(0, 4, 1):
        obj.sleepSec(1)
        ret = obj.get_reply_raw(qid, offset * pageSize, pageSize)
        if ret is not None:
            for sr in ret[u'data']:
                arrReplyList.append(sr)

        pass
    data[u'replyList'] = arrReplyList
    content = json.dumps(data, ensure_ascii=False)

    obj.saveFile(fileName, content)

#obj.getCommentList(url)




#ret = obj.get_reply_raw(21933888, 0, 10)
print 'finish...'

