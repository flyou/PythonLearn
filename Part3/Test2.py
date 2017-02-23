#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/23 19:54
# EMAIL fangjalylong@qq.com
# Desc  Error 处理
# --------------------------
import urllib2

repuest = urllib2.Request("http://XXX.xxxx.com")
try:
	response = urllib2.urlopen(repuest)
except urllib2.URLError, e:
	print e.reason
print response.read()
