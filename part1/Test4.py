#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/21 21:11
# EMAIL fangjalylong@qq.com
# Desc  Python列表
# --------------------------
'''
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。
列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
'''
list1=[1,"a",100.0,"c","d","e"]
list2=["hello","world"]

list2[1]="flyou";
print list1
print list1[0]
print list1[2:]
print list1[:2]
print list1[2:5]
print list1*2
print list1+list2