#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/21 21:38
# EMAIL fangjalylong@qq.com
# Desc Python 运算符
# --------------------------
print "-------------Python算术运算符----------------"
a = 25
b = 10
print a + b
print a - b
print a * b
print a / b
print a % b
print a // b

print "-------------Python比较运算符----------------"

if a > b:
    print "a>b"
elif a < b:
    print "a<b"
else:
    print "a=b"
if a <> b:
    print "a<>b"
if a >= b:
    print "a>=b"

print "------------Python赋值运算符----------------"

a = 10
b = 2

a = b
print a
a += b
print a
a -= b
print a
a *= b
print a
a /= b
print a
a %= b
print a
a **= b
print a
a //= b
print a
print "------------Python逻辑运算符----------------"

# 当值为0时为false
a = 0
b = 20
if a and b:
    print "a和b都为true"
if a or b:
    print "a和b至少有一个为true"
if not a:
    print "a 为false"
print "------------Python成员运算符----------------"

list1 = [0, 20, 30, 40, 50]
if a in list1:
    print "a in list1"
else:
    print "a not in list1"

if 60 not in list1:
    print "60 not in list1"
print "------------Python身份运算符----------------"
a = 20
b = 20

if a is b:
    print "a is b"
else:
    print "a is not b"

b=30
if a is b:
    print "a is b"
else:
    print "a is not b"
