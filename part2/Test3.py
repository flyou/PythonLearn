#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/22 22:15
# EMAIL fangjalylong@qq.com
# Desc Time
# --------------------------
import calendar
import time

print  time.time()
print time.asctime(time.localtime(time.time()))

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print calendar.month(2017, 2)
