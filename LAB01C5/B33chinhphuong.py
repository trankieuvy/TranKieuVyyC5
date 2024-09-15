# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:37:18 2024

@author: trankieuvy23717511

"""

n=int(input("Nhập vào số nguyên dương n: "))
if n<0:
    print("Số âm không thể là số chính phương")
else:
    i=0
    while i*i<=n:
        if i*i==n:
            print(n,"là số chính phương")
            break
        i+=1
    else:
        print(n,"không phải là số chính phương")
        
        