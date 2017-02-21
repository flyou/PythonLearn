#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/21 21:14
# EMAIL fangjalylong@qq.com
# Desc python元组
#元组是另一个数据类型，类似于List（列表）。
#元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# --------------------------

tuple1=("aaa","bbb","ccc","ddd","eee","fff")
tuple2=(1,2,3,4,5,6)

print tuple1
print tuple1[0]
print tuple1[:2]
print tuple1[2:]
print tuple1[2:5]
print tuple1*2
print tuple1+tuple2

