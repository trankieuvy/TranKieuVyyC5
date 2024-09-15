# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:12:59 2024

@author: trankieuvy
"""

n=int(input("Nhập vào số nguyên dương chẵn n:"))
if n<0 or n%2!=0:
    print("Vui lòng nhập lại số nguyên dương chẵn")
else:
    S=0
    i=2
    while i<=n:
        S+=i
        i+=2
    print("Tổng S=2+4+6+...+n là: ",S)
    
    
    

    
    