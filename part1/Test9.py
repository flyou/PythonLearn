#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author flyou
# Date 2017/2/21 21:58
# EMAIL fangjalylong@qq.com
# Desc 循环语句
# --------------------------
count = 0
while count <= 9:
    print "count is ", count
    count += 1

list1 = [0, 3, 7, 20, 19, 33, 64]
even = []
odd = []
while len(list1) > 0:
    number = list1.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print even
print odd
print '--------------------------------'
# var=1
# while var==1:
#     num=raw_input("please input a number")
#     print num
print '--------------------------------'

count=1
while count<5:
    print "count <5"
    count+=1
else:
    print "count>=5"

print '--------------------------------'

for letter in "flyou":
    print letter

list1=["a","b","c","d","e"]
for var in list1:
    print var


for index in range(len(list1)):
    print "当前:"+list1[index]


