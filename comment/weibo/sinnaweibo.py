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
        'Host': 'weibo.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Cookie': 'TC-Page-G0=1bbd8b9d418fd852a6ba73de929b3d0c; SUB=_2AkMtCQKTf8NxqwJRmP0WxWrmbYh0yQ3EieKbVfNIJRMxHRl-yT9jqhw6tRB6Bokse1XsWwHge0qona1KUgzAXRuWn-lK; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5QWXeIwOmhO8BaMblIKQsX'


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

    def getCommentHomePage(self, url):
        print 'getCommentHomePage...'
        randdom_header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        req = urllib2.Request(url)
        req.add_header("User-Agent", randdom_header)
        req.add_header("Host", "weibo.com")
        req.add_header("Upgrade-Insecure-Requests", "1")
        req.add_header("Accept-Language", "zh-cn")
        req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=utf-8")

        content = requests.get(url, verify=False, headers=self.header_info).content

        return content


    def getCommentListID(self, url):
        print 'getCommentList...'
        print url

        file_context = self.getCommentHomePage(url)
        #self.saveWeiBoHtml(file_context)
        #fileName = self.baseDir + "weibo_001.html"
        #file_object = open(fileName)
        #file_context = file_object.read()


        p = re.compile('\s+')
        #new_string = re.sub(p, '', file_context)
        #new_string = 'tion-data=id=4194068164440762&filter'
        #print file_context
        pattern = re.compile(r'action-data=\\\"id=\d+')
        matchObj = pattern.search(file_context)
        #print file_context
        new_content = matchObj.group()
        new_pattern = re.compile(r'\d+')
        new_matchObj = new_pattern.search(new_content)
        return new_matchObj.group()

    def getCID(self, content):
        print 'xx'

    def getWeiboCommentTmp(self, _id, _page):
        #fileName = self.baseDir + 'aad9fd2e6493febcbacae1589778a5ff.html'
        #fileObject = open(fileName)
        #fileContent = fileObject.read()

        __rnd = int(round(time.time() * 1000))
        url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&from=singleWeiBo&page=' + str(_page) + "&__rnd=" + str(
            __rnd) + "&id=" + str(_id)
        print url

        fileContent = self.getCommentHomePage(url)

        #arrContent = json.loads(fileContent)
        #arrData = json.loads(arrContent[u'commentList'][0])
        arrData = json.loads(fileContent)
        htmlContent = arrData[u'data'][u'html']
        #self.saveFile('aaaa.html', htmlContent)
        soup = BeautifulSoup(htmlContent, "html.parser")
        commentList = soup.find('div', {"class": "list_ul"})
        cl = soup.find_all('div', attrs={'class': 'list_li S_line1 clearfix'})
        arrCommentList = []
        for scl in cl:
            scl_soup = BeautifulSoup(str(scl), "html.parser")
            test = scl_soup.find('div', {"class": "WB_text"})
            commentText = test.get_text()
            maoHaoPos = commentText.find('：') + 1
            new_commentText = commentText[maoHaoPos:]
            if len(new_commentText) <= 0:
                continue
            list_con_soup = scl_soup.find('div', {"class": "WB_media_wrap clearfix"})
            str_list_con_soup = str(list_con_soup)
            img_soup = BeautifulSoup(str_list_con_soup, "html.parser")
            img_list = img_soup.find_all('img', attrs={'att': ''})
            arr_img_url = []
            for s_img in img_list:
                img_url = 'https:' + s_img['src']
                img_url = img_url.replace('/thumb180/', '/large/');
                arr_img_url.append(img_url)

            tmpComment = {
                'text' : new_commentText,
                'imgList': arr_img_url
            }
            arrCommentList.append(tmpComment)

        print arrCommentList

        return arrCommentList
        for a in aAll:
            print self.baseUrl + a['href']
            jiJiuName = a.text
            print jiJiuName
            self.save_single_page(self.baseUrl + a['href'], jiJiuName)

        __rnd = int(round(time.time() * 1000))
        print __rnd
        url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&from=singleWeiBo&page=' + str(_page) + "&__rnd=" + str(__rnd) + "&id=" + str(_id)
        print url

        content = self.getCommentHomePage(url)
        return content

    def getWeiboComment(self, _id, _page):
        #fileName = self.baseDir + 'aad9fd2e6493febcbacae1589778a5ff.html'
        #fileObject = open(fileName)
        #fileContent = fileObject.read()

        __rnd = int(round(time.time() * 1000))
        url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&from=singleWeiBo&page=' + str(_page) + "&__rnd=" + str(
            __rnd) + "&id=" + str(_id)
        print url

        fileContent = self.getCommentHomePage(url)

        #arrContent = json.loads(fileContent)
        #arrData = json.loads(arrContent[u'commentList'][0])
        arrData = json.loads(fileContent)
        htmlContent = arrData[u'data'][u'html']
        #self.saveFile('aaaa.html', htmlContent)
        soup = BeautifulSoup(htmlContent, "html.parser")
        commentList = soup.find('div', {"class": "list_ul"})
        cl = soup.find_all('div', attrs={'node-type': 'root_comment'})
        arrCommentList = []
        for scl in cl:
            scl_soup = BeautifulSoup(str(scl), "html.parser")
            test = scl_soup.find('div', {"class": "WB_text"})
            commentText = test.get_text()
            maoHaoPos = commentText.find('：') + 1
            new_commentText = commentText[maoHaoPos:]
            if len(new_commentText) <= 0:
                continue
            list_con_soup = scl_soup.find('div', {"class": "WB_media_wrap clearfix"})
            str_list_con_soup = str(list_con_soup)
            img_soup = BeautifulSoup(str_list_con_soup, "html.parser")
            img_list = img_soup.find_all('img', attrs={'att': ''})
            arr_img_url = []
            for s_img in img_list:
                img_url = 'https:' + s_img['src']
                img_url = img_url.replace('/thumb180/', '/large/');
                arr_img_url.append(img_url)

            tmpComment = {
                'text' : new_commentText,
                'imgList': arr_img_url
            }
            arrCommentList.append(tmpComment)

        print arrCommentList

        return arrCommentList
        for a in aAll:
            print self.baseUrl + a['href']
            jiJiuName = a.text
            print jiJiuName
            self.save_single_page(self.baseUrl + a['href'], jiJiuName)

        __rnd = int(round(time.time() * 1000))
        print __rnd
        url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&from=singleWeiBo&page=' + str(_page) + "&__rnd=" + str(__rnd) + "&id=" + str(_id)
        print url

        content = self.getCommentHomePage(url)
        return content

    def saveWeiBoHtml(self, content):
        self.makeDir(self.baseDir)

        fileName = self.baseDir + "weibo_001.html"
        self.writeLog("save file :" + str(fileName))

        fileHandle = open(fileName, 'a')

        fileHandle.write(content + "\n")
        fileHandle.close()

    def saveWeiBoContent(self, inputData):
        print 'saveWeiBoContent...'
        title = inputData[u'title']
        url = inputData[u'url']
        inputData[u'commentList'] = []

        id = self.getCommentListID(url)
        inputData[u'id'] = id

        for pageNum in range(1, 5, 1):
            self.sleepSec(1)
            commentList = self.getWeiboCommentTmp(id, pageNum)
            #inputData[u'commentList'].append(self.getWeiboComment(id, pageNum))
            for scmt in commentList:
                print 'append comment...'
                inputData[u'commentList'].append(scmt)

        hash_md5 = hashlib.md5(url)
        str_md5 = hash_md5.hexdigest()
        fileName = self.baseDir + str(str_md5) + str(".html")
        print fileName
        content = json.dumps(inputData, ensure_ascii=False)
        self.saveFile(fileName, content)
        #id = self.getCommentListID(url)



print 'start...'

obj = CSpider();

url = "https://weibo.com/1713926427/FDt8QiDfc?from=page_1005051713926427_profile&wvr=6&mod=weibotime&type=comment#_rnd1515490268828"

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

#content = json.dumps(arrQuestionList, ensure_ascii=False)

for inputData in arrQuestionList:
    data = json.loads(inputData)
    obj.saveWeiBoContent(data)

#obj.getCommentList(url)

print 'finish...'

