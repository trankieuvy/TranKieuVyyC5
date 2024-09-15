# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:36:47 2024

@author: trankieuvy
"""

for z in range(1, 979 // 9 + 1):  
    for y in range(1, (979 - 9 * z) // 7 + 1):
        x =(979-7*y-9*z)//2
    if x>0 and x.is_integer():
        print("Nghiệm của phương trình là: ","x= ",int(x),"y=",y,"z=",z)
        