# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:33:14 2024

@author: trankieuvy
"""

n=int(input("Nhập  số n: "))
S=0
for i in range (n):
    S+=1/(2*i+1)
print("Tổng S=1+1/3+1/5+...+1/2n+1 là :",S)