# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:28:21 2024

@author: trankieuvy
"""

n=int(input("Nhập vaò số n: "))
S=0
for i in range (1,n+1):
    S+=1/2*i
print("Tổng S=1/2+1/4+...+1/2n là: ",S)