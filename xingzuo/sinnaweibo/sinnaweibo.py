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

reload(sys)

sys.setdefaultencoding('utf-8')

class CSpider:
    '''spider'''
    baseDir = './crawl_data/'
    baseUrl = 'http://www.a-hospital.com'
    #091e9c5e808e80c8
    baseID = '091e9c5e808e'
    # [20672,36035]
    subID = 36035

    #random.choice(srandTime)
    srandTime = [
        1,
    ]

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

    def getWeiBoDetail(self, url):
        randdom_header = "Weibo/8497 (iPhone; iOS 10.3.3; Scale/2.00)"

        req = urllib2.Request(url)
        req.add_header("User-Agent", randdom_header)
        req.add_header("Host", "api.weibo.cn")
        req.add_header("X-Log-Uid", "1784034593")
        req.add_header("Accept-Language", "zh-cn")
        req.add_header("X-Validator", "9lwg1x4Upm9Xwl5UPd7U08l2DRkzsvrhXvinkqLNZD8=")
        req.add_header("Content-Type","application/x-www-form-urlencoded; charset=utf-8")
        req.add_header("X-Sessionid","70D1436E-5858-443F-A454-22DC1364DE46")

        req.add_header("GET", url)

        #context = ssl._create_unverified_context()
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

        content = urllib2.urlopen(req, context=context).read()
        #arrAns = json.loads(content)


        #html = requests.get(url)
        #content = html.content
        return content

    def getWeiBoDetail666(self, url):
        randdom_header = "Weibo/8497 (iPhone; iOS 10.3.3; Scale/2.00)"

        req = urllib2.Request(url)
        req.add_header("User-Agent", randdom_header)
        req.add_header("Host", "api.weibo.cn")
        req.add_header("X-Log-Uid", "1784034593")
        req.add_header("Accept-Language", "zh-cn")
        req.add_header("X-Validator", "9lwg1x4Upm9Xwl5UPd7U08l2DRkzsvrhXvinkqLNZD8=")
        req.add_header("Content-Type","application/x-www-form-urlencoded; charset=utf-8")
        req.add_header("X-Sessionid","70D1436E-5858-443F-A454-22DC1364DE46")

        req.add_header("GET", url)

        context = ssl._create_unverified_context()
        #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

        content = urllib2.urlopen(req, context=context).read()
        #arrAns = json.loads(content)


        #html = requests.get(url)
        #content = html.content
        return content

    def run(self, url, authorName):
        print 'run...'
        print authorName
        print url

        self.sleepSec(1);

        content = self.getWeiBoDetail(url);

        arrContent = json.loads(content)

        rowCt = 0

        for card in arrContent['cards']:
            try:
                text = card['mblog']['text']
                print text
                mid = card['mblog']['mid']
                href = "http://weibo.com/p/aj/mblog/getlongtext?mid=" + str(mid)
                self.saveConstellationArticleTitle(authorName, text)

                rowCt = 1

            except Exception, e:
                print e
                print 'execpt...'

        return rowCt

    def getArticle(self, url):
        print 'get article...'
        print url

        html = self.getHtml(url)
        content = html.content
        soup = BeautifulSoup(content, "html.parser")
        artibody = soup.find('div', {"id": "artibody"})

        return str(artibody)

    def saveConstellationArticleTitle(self, constellationTitle, content):
        self.makeDir(self.baseDir)

        fileName = self.baseDir + constellationTitle + ".txt"
        self.writeLog("save file :" + str(fileName))

        fileHandle = open(fileName, 'a')

        print content
        fileHandle.write(content + "\n")
        fileHandle.close()


    def saveConstellationArticle(self, fileTitle, content):
        self.makeDir(self.baseDir)

        fileName = self.baseDir + fileTitle + ".json"
        self.writeLog("save file :" + str(fileName))

        fileHandle = open(fileName, 'w')

        arrPV = {
            "constellation": content['constellation'],
            "constellationHref": content['constellationHref'],
            "constellationArticleTitle": content['constellationArticleTitle'],
            "constellationArticleContent": str(content['constellationArticleContent']),
            "constellationArticleHref": content['constellationArticleHref'],
        }

        content = json.dumps(arrPV, ensure_ascii=False)
        fileHandle.write(content + "\n")
        fileHandle.close()


print 'begin..'

url = "http://feed.mix.sina.com.cn/api/roll/get?pageid=25&lid=405&num=10&page=1";
url = "https://api.weibo.cn/2/cardlist?networktype=wifi&wm=3333_2001&i=df4a735&sflag=1&b=1&skin=default&c=iphone&v_p=50&v_f=1&lang=zh_CN&s=684797f6&from=1079193010&ua=iPhone5,2__weibo__7.9.1__iphone__os10.3.3&ft=0&aid=01AsUQYLzWqS1kZ67ke9CJETrFIY4b6k7CmrE2MRT19Unmpzc.&gsid=_2A250skirDeRxGedJ41YR8yrJwj-IHXVV5ttjrDV6PUJbkdANLUzwkWoJ5owpc8s_Cg8Xl-ydHnn8F8EFXw..&extparam=100103q%3Dal%26t%3D2&moduleID=pagecard&luicode=10000003&page=2&containerid=1076031680990025&fid=1076031680990025&need_head_cards=0&featurecode=10000085&uicode=10000198&count=20"


obj = CSpider();

author = {
    "Alex是大叔",
    "同道大叔",
    "星座小王子",
    "新浪星座",
    "占星小巫爱星座",
}

url = "http://weibo.com/p/aj/mblog/getlongtext?ajwvr=6&mid=4148186702105850&is_settop&is_sethot&is_setfanstop&is_setyoudao&__rnd=1505114271874"


for authorName in author:
    print authorName

authorName = "Alex是大叔"
page = 1;
while False:
    url = "https://api.weibo.cn/2/cardlist?networktype=wifi&wm=3333_2001&i=df4a735&sflag=1&b=1&skin=default&c=iphone&v_p=50&v_f=1&lang=zh_CN&s=684797f6&from=1079193010&ua=iPhone5,2__weibo__7.9.1__iphone__os10.3.3&ft=0&aid=01AsUQYLzWqS1kZ67ke9CJETrFIY4b6k7CmrE2MRT19Unmpzc.&gsid=_2A250skirDeRxGedJ41YR8yrJwj-IHXVV5ttjrDV6PUJbkdANLUzwkWoJ5owpc8s_Cg8Xl-ydHnn8F8EFXw..&extparam=100103q%3Dal%26t%3D2&moduleID=pagecard&luicode=10000003&page=" + str(
        page) + "&containerid=1076031680990025&fid=1076031680990025&need_head_cards=0&featurecode=10000085&uicode=10000198&count=20"
    rowCT = obj.run(url, authorName);
    page = page + 1
    if rowCT == 0:
        break;


page = 1;
authorName = "同道大叔"
while False:
    url = "https://api.weibo.cn/2/cardlist?networktype=wifi&wm=3333_2001&i=df4a735&sflag=1&b=1&skin=default&c=iphone&v_p=50&v_f=1&lang=zh_CN&s=684797f6&from=1079193010&ua=iPhone5,2__weibo__7.9.1__iphone__os10.3.3&ft=0&aid=01AsUQYLzWqS1kZ67ke9CJETrFIY4b6k7CmrE2MRT19Unmpzc.&gsid=_2A250skirDeRxGedJ41YR8yrJwj-IHXVV5ttjrDV6PUJbkdANLUzwkWoJ5owpc8s_Cg8Xl-ydHnn8F8EFXw..&featurecode=10000085&mid=4150521130169289&need_head_cards=0&containerid=1076033069348215&fid=1076033069348215&lcardid=seqid%3A99877413%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-2-0%7Cq%3A%E5%90%8C%E9%81%93%E5%A4%A7%E5%8F%94%7Cext%3A%26cate%3D26%26mid%3D4150521130169289%26&rid=0_0_0_2676178600129913717&_status_id=4150521130169289&page=" + str(page) + "&lfid=230926type%3D1%26q%3D%E5%90%8C%E9%81%93%E5%A4%A7%E5%8F%94%26t%3D0&luicode=10000003&count=20&moduleID=pagecard&uicode=10000198"
    rowCT = obj.run(url, authorName);
    page = page + 1
    if rowCT == 0:
        break;


############
page = 62;
authorName = "星座小王子"
while False:
    url = "https://api.weibo.cn/2/cardlist?networktype=wifi&wm=3333_2001&i=df4a735&sflag=1&b=1&skin=default&c=iphone&v_p=50&v_f=1&lang=zh_CN&s=684797f6&from=1079193010&ua=iPhone5,2__weibo__7.9.1__iphone__os10.3.3&ft=0&gsid=_2A250skirDeRxGedJ41YR8yrJwj-IHXVV5ttjrDV6PUJbkdANLUzwkWoJ5owpc8s_Cg8Xl-ydHnn8F8EFXw..&aid=01AsUQYLzWqS1kZ67ke9CJETrFIY4b6k7CmrE2MRT19Unmpzc.&featurecode=10000085&sourcetype=page&need_head_cards=0&containerid=1076031197071940&fid=1076031197071940&lcardid=1001030111_seqid%3A409419490%7Ctype%3A1%7Ct%3A1%7Cpos%3A1-0-0%7Cq%3A%E6%98%9F%E5%BA%A7%E5%B0%8F%E7%8E%8B%E5%AD%90%7Cext%3A%26cate%3D1%26uid%3D1197071940%26&page="+str(page)+"&lfid=100103type%3D1%26q%3D%E6%98%9F%E5%BA%A7%E5%B0%8F%E7%8E%8B%E5%AD%90%26t%3D1&luicode=10000003&count=20&moduleID=pagecard&uicode=10000198"
    rowCT = obj.run(url, authorName);
    page = page + 1
    if rowCT == 0:
        break;

############
page = 1;
authorName = "新浪星座"
while True:
    url = "https://api.weibo.cn/2/cardlist?networktype=wifi&wm=3333_2001&i=df4a735&sflag=1&b=1&skin=default&c=iphone&v_p=50&v_f=1&lang=zh_CN&s=684797f6&from=1079193010&ua=iPhone5,2__weibo__7.9.1__iphone__os10.3.3&ft=0&gsid=_2A250skirDeRxGedJ41YR8yrJwj-IHXVV5ttjrDV6PUJbkdANLUzwkWoJ5owpc8s_Cg8Xl-ydHnn8F8EFXw..&aid=01AsUQYLzWqS1kZ67ke9CJETrFIY4b6k7CmrE2MRT19Unmpzc.&featurecode=10000085&sourcetype=page&need_head_cards=0&containerid=1076031644291782&fid=1076031644291782&lcardid=1001030111_seqid%3A789514857%7Ctype%3A1%7Ct%3A1%7Cpos%3A1-0-0%7Cq%3A%E6%96%B0%E6%B5%AA%E6%98%9F%E5%BA%A7%7Cext%3A%26cate%3D1%26uid%3D1644291782%26&page="+str(page)+"&lfid=100103type%3D1%26q%3D%E6%96%B0%E6%B5%AA%E6%98%9F%E5%BA%A7%26t%3D1&luicode=10000003&count=20&moduleID=pagecard&uicode=10000198"
    rowCT = obj.run(url, authorName);
    page = page + 1
    if rowCT == 0:
        break;

###########################
page = 1;
authorName = "占星小巫爱星座"
while False:
    url = "https://api.weibo.cn/2/cardlist?networktype=wifi&wm=3333_2001&i=df4a735&sflag=1&b=1&skin=default&c=iphone&v_p=50&v_f=1&lang=zh_CN&s=684797f6&from=1079193010&ua=iPhone5,2__weibo__7.9.1__iphone__os10.3.3&ft=0&gsid=_2A250skirDeRxGedJ41YR8yrJwj-IHXVV5ttjrDV6PUJbkdANLUzwkWoJ5owpc8s_Cg8Xl-ydHnn8F8EFXw..&aid=01AsUQYLzWqS1kZ67ke9CJETrFIY4b6k7CmrE2MRT19Unmpzc.&featurecode=10000085&sourcetype=page&lon=116.268860104672&containerid=1076032154332097&need_head_cards=0&fid=1076032154332097&lcardid=1001030111_seqid%3A680536856%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E5%8D%A0%E6%98%9F%E5%B0%8F%E5%B7%AB%E7%88%B1%E6%98%9F%E5%BA%A7%7Cext%3A%26cate%3D1%26uid%3D2154332097%26&lat=40.04283096483412&page="+str(page)+"&offset=1&lfid=100103type%3D1%26q%3D%E5%8D%A0%E6%98%9F%E5%B0%8F%E5%B7%AB%E7%88%B1%E6%98%9F%E5%BA%A7%26t%3D0&luicode=10000003&count=20&moduleID=pagecard&uicode=10000198"
    rowCT = obj.run(url, authorName);
    page = page + 1
    if rowCT == 0:
        break;
#url = "http://astro.sina.com.cn/v/ss/2017-09-07/doc-ifykusey4488153-p2.shtml"
#obj.getArticle(url)
print 'end......'
