# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:52:46 2024

@author: trankieuvy
"""

n=int(input("Nhập số nguyên dương n: "))
if n<0:
    print("n không phải là số nguyên dương")
elif n>0:
    S=0
    i=1
    while i<=n:
        S+=i
        i+=1
    print("Tổng S=1+2+3+...+n= ",S)
        