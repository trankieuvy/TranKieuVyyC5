# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:01:23 2024

@author: trankieuvy
"""

n=int(input("Nhập vào số nguyên dương: "))
while n<0:
    n=int(input("Vui lòng nhập lại số nguyên dương:"))
else:
    for i in range(1,n+1):
        if n%i==0:
            uoc=i

            print("Các ước của số ",n,"là:",uoc)
            
    
    