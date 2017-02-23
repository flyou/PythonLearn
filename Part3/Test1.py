#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/23 19:36
# EMAIL fangjalylong@qq.com
# Desc 
# --------------------------
import urllib
import urllib2

# response = urllib2.urlopen("http://www.baidu.com/")
# print  response.read()

# 构建request

# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()

# Post传参数

# values = {"username":"fangjaylong@qq.com","password":"XXX"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()

# Get传参数
# values = {}
# values['username'] = "fangjaylong@qq.com"
# values['password'] = "553274238"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?" + data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print response.read()

# 设置Headers

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username' : 'cqc',  'password' : 'XXXX' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
