# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:18:42 2024

@author: trankieuvy
"""

n=int(input("Nhập vào số nguyên dương lẻ n:"))
if n<0 or n%2==0:
    print("Vui lòng nhập lại số nguyên dương lẻ")
else:
    S=1
    i=1
    while i<=n:
        S*=i
        i+=1
    print("Tổng S=1*2*3*...*n là: ",S)
    
    