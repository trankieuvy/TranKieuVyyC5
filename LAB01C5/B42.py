# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:39:15 2024

@author: trankieuvy
"""

n=int(input("Nhập  số n: "))
S=0
for i in range (1,n+1):
    S+=1/i*(i+1)
print("Tổng S=1/1*2 +1/1*3 +...+ 1/n*(n+1) là:",S)