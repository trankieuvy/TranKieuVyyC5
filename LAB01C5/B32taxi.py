# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:11:15 2024

@author: trankieuvy
"""
#TAXI 
sokm=int(input("Nhập vào số km đã đi được: "))
tong=0
if sokm==1:
    tong=sokm*15000
elif 2 <= sokm <= 5:
    tong = 15000 + (sokm - 1) * 13500
elif sokm >= 6:
    tong= 15000 + (sokm - 4) * 13500 + (sokm-5) * 11000
elif sokm > 120:
    tong= (15000 + (sokm - 4) * 13500 + ((sokm-5) * 11000))* 0.9
print("số km đã đi là:", sokm,"và số tiền phải trả là: ",tong)
    

        
