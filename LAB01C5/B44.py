# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:45:43 2024

@author: trankieuvy
"""

n=int(input("Nhập  số n: "))
S=0
for i in range (1,n+1):
    S+=(2*i + 1)/(2*i + 2)
print("Tổng S=1/2+3/4+...+(2n+1)/(2n+2) là: ",S)
