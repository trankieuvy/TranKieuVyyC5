# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:40:18 2024

@author: Admin
"""

x=float(input("Nhập vào một số thực trong khoảng[-89.9,88.8]: "))
while x<-89.9 or x>88.8:
    
    x=float(input("Vui lòng nhập lại x: "))
print("Số đã nhập vào là: ",x)
    