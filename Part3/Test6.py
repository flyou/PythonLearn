#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/25 1:10
# EMAIL fangjalylong@qq.com
# Desc requests 和BeautifulSoup结合使用
#         抓取糗事百科为例
# --------------------------
import codecs
from time import sleep

import requests
from bs4 import BeautifulSoup

BASE_URL="http://www.qiushibaike.com/"
URL_HOT="hot/"
URL_IMGRANK="imgrank/"
URL_PIC="pic/"
URL_TEXT="text/"
URL_HISTORY="history/"
URL_NEW="textnew/"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
position = 1
def getTextByPage(page):
    r = requests.get(BASE_URL+URL_TEXT+str(page), headers=headers)
    soup=BeautifulSoup(r.text,"html5lib")
    try:
        qiubaiList= soup.select_one("#content-left").find_all("div",class_="content")
    except BaseException:
        print "异常:", page
        return
    else:
        global position
        for text in qiubaiList:
            file.write(str(position)+":"+text.span.text+"")
            file.write("\n\n--------------------\n\n")
            position +=1
        print "获取该页数据成功:", page


    return

def getPageNumber():
    r = requests.get(BASE_URL + URL_TEXT + str(page), headers=headers)
    soup = BeautifulSoup(r.text, "html5lib")
    pages=soup.select("span .page-numbers")
    print pages.text

if __name__ == '__main__':
    file = codecs.open("flyou.txt", "wb+", "utf-8")
    page=1
    for x in range(35):

        getTextByPage(page)
        page+=1
        sleep(0.5)
    file.close()
    print "所有页面抓取完成"



