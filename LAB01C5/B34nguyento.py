# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:46:31 2024

@author: trankieuvy
"""

n=int(input("Nhập số nguyên dương n:"))
if n<=1:
    print("Không phải là số nguyên tố")
else:
    i=2
    while i*i<=n:
        if n%i==0:
            print(n,"không phải là số nguyên tố")
            break
        i+=1
    else:
        print(n,"là số nguyên tố")
        