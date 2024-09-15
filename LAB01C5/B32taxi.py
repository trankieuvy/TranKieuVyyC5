# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:11:15 2024

@author: trankieuvy
"""
sokm=int(input("Nhập số km đã đi được: "))
sotien=0
for i in range(1,sokm+1):
    if i==1:
        sotien+=15000
    elif 2<=i<=5:
        sotien+=13500
    else:
        sotien+=11000
if i>120:
    sotien*=0.9
print("Số km đã đi là ",sokm,"km và số tiền cần phải thanh toán là",sotien,"VND")

        