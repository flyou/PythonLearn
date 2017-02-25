#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/25 14:42
# EMAIL fangjalylong@qq.com
# Desc 
# --------------------------
import codecs

import jieba.analyse

jieba.initialize()

file = codecs.open("flyou.txt", "r", "utf-8")
content = file.read()
try:
	tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
	for item in tags:
		print(item[0] + '\t' + str(int(item[1] * 1000)))

finally:
	file.close()
