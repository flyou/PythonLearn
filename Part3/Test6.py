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

import getIP

BASE_URL = "http://www.qiushibaike.com/"
URL_8HR= "8hr/"
URL_HOT = "hot/"
URL_IMGRANK = "imgrank/"
URL_TEXT = "text/"
URL_HISTORY = "history/"
URL_NEW = "textnew/"
qiuBaiType=[URL_8HR,URL_HOT,URL_IMGRANK,URL_TEXT,URL_NEW]
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
position = 1
def getTextByPage(page,type):
	# 获取段子列表
	r = requests.get(BASE_URL + type + str(page), headers=headers,proxies=getRandomIp())
	soup = BeautifulSoup(r.text, "html5lib")
	try:
		qiubaiList = soup.select_one("#content-left").find_all("div", class_="content")
	except BaseException:
		print "异常:", page
		return
	else:
		global position
		for text in qiubaiList:
			file.write(str(position) + ":" + text.span.text + "")
			file.write("\n\n--------------------\n\n")
			position += 1
		print "获取"+type+"数据成功,页码:", page

	return
def getPageNumber():
	# 获取页面总页数
	r = requests.get(BASE_URL + URL_TEXT, headers=headers,proxies=getRandomIp())
	soup = BeautifulSoup(r.text, "html5lib")
	pages = soup.select("span.page-numbers")
	return pages[len(pages) - 1].text

def getRandomIp():


	ip_list = getIP.get_ip_list()
	proxies = getIP.get_random_ip(ip_list)
	return proxies

if __name__ == '__main__':
	for type in qiuBaiType:
		totalPage = getPageNumber()
		file = codecs.open(type[0:len(type)-1]+".txt", "wb+", "utf-8")
		currentPage = 1

		for x in range(int(totalPage)):
			getTextByPage(currentPage,type)
			currentPage += 1
			sleep(1)
		print type+"页面所有数据抓取完成"
		file.flush()
		file.close()


