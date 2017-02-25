#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/22 22:45
# EMAIL fangjalylong@qq.com
# Desc 函数调用
# --------------------------
def printStr(name, age):
    print name
    print age


def printStr1(name, age=100):
    print name
    print age

#
# if __name__ == '__main__':
#     printStr("100", 10)
#     printStr(name="1000", age=10)
# printStr1(name=100)
# sum1 =lambda num1,num2:num1+num2
#
# print  sum1(10,20)