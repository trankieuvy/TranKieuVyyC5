# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:12:21 2024

@author: Admin
"""
x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))

while y != 0:
  a=x%y
  x=y
  y=a

print("Ước chung lớn nhất của hai số là: {}".format(x))