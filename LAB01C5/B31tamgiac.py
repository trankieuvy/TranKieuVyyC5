# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:00:21 2024

@author: trankieuvy
"""

a=int(input("Nhập vào số thứ nhất: "))
b=int(input("Nhập vào số thứ hai: "))
c=int(input("Nhập vào số thứ ba: "))
while a<0 and b<0 and c<0:
    print("Lỗi,ba số không phải là số nguyên dương")
else:
    if a==b==c:
        print("Tam giác đều")
    elif a==b or a==c or b==c:
        print("Tam giác cân")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
        
    