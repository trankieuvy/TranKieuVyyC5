# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:17:35 2024

@author: trankieuvy
"""

n=int(input("Nhập vào số nguyên dương: "))
tong= 0
while n>0:
        tong += n%10
        n//=10
        
print("Tổng các chữ số là:",tong)
        
        
