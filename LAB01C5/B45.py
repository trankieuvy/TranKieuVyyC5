# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:51:03 2024

@author: trankieuvy
"""

x=int(input("Nhập vào số x: "))
n=int(input("Nhập vào số n: "))
S=x
mauso=n
for i in range(2,n+1):
    mauso +=1
    S += x**i/mauso

print("Tổng S(n)=x+ x^2/1+2 + x^3/1+2+3 + ...+ x^n/1+2+3+...+n là : ",S)
