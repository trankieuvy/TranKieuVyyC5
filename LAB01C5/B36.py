# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:03:16 2024

@author: trankieuvy
"""

n=int(input("Nhập vào số nguyên dương n:"))
if n<0:
    print("n không phải là số nguyên dương")
elif n>0:
    S=0
    i=1
    while i<=n:
        S+=i*i
        i+=1
        
    print("Tổng S=1^2+2^2+3^2+...+n^2 là: ",S)
        
    