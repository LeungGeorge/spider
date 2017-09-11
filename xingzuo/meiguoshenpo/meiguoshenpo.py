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

    def run(self, url):
        print 'get_url...'
        print url;
        html = self.getHtml(url)
        content = html.content
        soup = BeautifulSoup(content, "html.parser")

        fileName = "constellationTitle.txt"

        # 顶部
        divs = soup.findAll('div', {"class": "head_2"})
        for a in divs:
            li = a.findAll('li')
            for aa in li:
                singleA = aa.findAll('a');
                for sa in singleA:
                    self.saveConstellationArticleTitle(fileName, sa['title'])

        divs = soup.find('div', {"class": "wrapper xz_box"})

        for child in divs:
            try:
                # 获取星座名，链接
                h4 = child.find('h4')
                fileTitle = ''
                h4Text = ''
                liText = ''
                if h4 is not None:
                    h4Href = h4.a['href']
                    h4Text = h4.a.get_text()

                # 获取星座问题
                lis = child.findAll('li')
                for li in lis:
                    liHref = li.a['href']
                    liText = li.a.get_text()

                    articleContent = self.getArticle(liHref)

                    constellationContent = {
                        "constellation": h4Text,
                        "constellationHref": h4Href,
                        "constellationArticleTitle": liText,
                        "constellationArticleContent": articleContent,
                        "constellationArticleHref": liHref,
                    }

                    self.saveConstellationArticleTitle(fileName, liText)
                    #fileTitle = h4Text + str('------') + liText
                    #self.saveConstellationArticle(fileTitle, constellationContent)

            except Exception, e:
                print e
                print 'execpt...'
            finally:
                pass

    def getArticle(self, url):
        print 'get article...'
        print url

        html = self.getHtml(url)
        content = html.content
        soup = BeautifulSoup(content, "html.parser")
        show_cnt = soup.find('div', {"class": "show_cnt"})
        return str(show_cnt)

    def saveConstellationArticleTitle(self, constellationTitle, content):
        self.makeDir(self.baseDir)

        fileName = self.baseDir + constellationTitle
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
        print content
        fileHandle.write(content + "\n")
        fileHandle.close()


print 'begin..'

url = "http://www.meiguoshenpo.com/xingzuo/";

obj = CSpider();
obj.run(url);

print 'end......'
