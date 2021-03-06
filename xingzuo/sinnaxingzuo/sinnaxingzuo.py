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
        return html

    def run(self, constellation):
        print 'run...'

        for con in constellation:
            #'白羊座': {'id':25,'lid':405},
            pageid = constellation[con]['id']
            lid = constellation[con]['lid']
            page = 1;
            if pageid == 36:
                page = 21;

            while True:
                url = "http://feed.mix.sina.com.cn/api/roll/get?pageid=" + str(pageid) + "&lid=" + str(lid) + "&num=10&page=" + str(page);
                print url;

                html = self.getHtml(url)
                content = html.content

                pjs = json.loads(content);

                rowCount = 0

                for row in pjs['result']['data']:
                    rowCount = rowCount + 1
                    oid = row['oid']
                    title = row['title']
                    intro = row['intro']
                    wapsummary = row['wapsummary']

                    url = row['url']

                    articleContent = self.getArticle(url)

                    constellationContent = {
                        "constellation": con,
                        "constellationHref": '',
                        "constellationArticleTitle": title,
                        "constellationArticleContent": articleContent,
                        "constellationArticleHref": url,
                    }

                    fileTitle = con + str('------') + str(oid) + str('------') + title
                    self.saveConstellationArticle(fileTitle, constellationContent)

                page = page + 1
                if rowCount == 0:
                    break;

    def getArticle(self, url):
        print 'get article...'
        print url

        html = self.getHtml(url)
        content = html.content
        soup = BeautifulSoup(content, "html.parser")
        artibody = soup.find('div', {"id": "artibody"})

        return str(artibody)

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

constellation = {
    '白羊座': {'id':25,'lid':405},
    '金牛座': {'id':26,'lid':413},
    '双子座': {'id':27,'lid':418},
    '巨蟹座': {'id':28,'lid':422},
    '狮子座': {'id':29,'lid':427},
    '处女座': {'id':30,'lid':432},
    '天秤座': {'id':31,'lid':437},
    '天蝎座': {'id':32,'lid':442},
    '射手座': {'id':33,'lid':447},
    '摩羯座': {'id':34,'lid':453},
    '水瓶座': {'id':35,'lid':458},
    '双鱼座': {'id':36,'lid':463},
}

constellationa = {
    #'白羊座': {'id':25,'lid':405},
    #'金牛座': {'id':26,'lid':413},
    #'双子座': {'id':27,'lid':418},
    #'巨蟹座': {'id':28,'lid':422},
    #'狮子座': {'id':29,'lid':427},
    #'处女座': {'id':30,'lid':432},
    ####'天秤座': {'id':31,'lid':437},
    #'天蝎座': {'id':32,'lid':442},
    #'射手座': {'id':33,'lid':447},
    #'摩羯座': {'id':34,'lid':453},
    #'水瓶座': {'id':35,'lid':458},
    '双鱼座': {'id':36,'lid':463},
}

obj = CSpider();

obj.run(constellationa);

#obj.run(constellation);

#url = "http://astro.sina.com.cn/v/ss/2017-09-07/doc-ifykusey4488153-p2.shtml"
#obj.getArticle(url)
print 'end......'
