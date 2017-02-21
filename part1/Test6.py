#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/21 21:26
# EMAIL fangjalylong@qq.com
# Desc Python 字典
# --------------------------
'''
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict1={'name':'flyou','age':24,'sex':'man'}

print dict1
print dict1['name']
print dict1.keys()
print dict1.values()

