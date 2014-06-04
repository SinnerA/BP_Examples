#coding=utf-8
def change(n):
    n[0] = "Mr Gumby"

names = ["Mrs Entity", "Mrs Thing"]
n = names[:]#切片操作创建一个副本
change(n)
print names

change(names)
print names

help(zip)

