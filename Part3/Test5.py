#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/25 0:24
# EMAIL fangjalylong@qq.com
# Desc BeautifulSoup的用法
# --------------------------
import requests
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
BASE_URL = "http://httpbin.org/"

r = requests.get(BASE_URL)
soup = BeautifulSoup(r.text, "html5lib")

# print soup.body['id']
# print soup.body.get('id')

# print soup.body.contents

# for child in  soup.body.children:
#     print child

# for child in soup.descendants:
#     print child

# print soup.body.div.ul.find