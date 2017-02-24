#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/24 16:08
# EMAIL fangjalylong@qq.com
# Desc requests 的用法
# --------------------------
import requests

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get("http://www.baidu.com", headers=headers)

print  r.text
