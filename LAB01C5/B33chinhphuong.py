# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:37:18 2024

@author: trankieuvy23717511

"""
import math
n=int(input("Nhập vào số nguyên dương n: "))
while n<= 0:
    n= int(input("Nhập lại n"))
if math.sqrt(n) == int(math.sqrt(n)):
    print("n là số chính phương")
else:
    print("n không phải là số chính phương")
    
    

