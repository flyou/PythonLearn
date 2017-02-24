#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/23 20:22
# EMAIL fangjalylong@qq.com
# Desc 
# --------------------------

import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/joke' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
	request = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(request)
	print response.read()
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
