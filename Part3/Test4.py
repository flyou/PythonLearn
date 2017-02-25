#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/24 16:08
# EMAIL fangjalylong@qq.com
# Desc requests 的用法
# --------------------------

import requests

BASE_URL = "http://httpbin.org/"
param = {"name": "flyou", "age": 24}

# --------------------------
# request=requests.get("http://httpbin.org/")
# print request.text
# --------------------------
# r=requests.get("http://httpbin.org/get")
# print r.text
# --------------------------

# r = requests.get("http://httpbin.org/get", params=param)
# print r.text
# --------------------------

# r=requests.post(BASE_URL+"post",param)
# print  r.text
# --------------------------

# header = {"User-Agent": "flyou_pc"}
# r = requests.post(BASE_URL + "post",data=param,headers=header)
# print r.text
# --------------------------

# r=requests.post(BASE_URL+"post",data=json.dumps(param))
# print r.text
# --------------------------
# file = open("flyou.text", "w+")
# file.write("flyou")
#
# files = {"file": file}
# r = requests.post(BASE_URL + "post", files=files)
# file.close()
# print r.text
