# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:25:57 2024

@author: Admin
"""

count=0
for i in range(1000,2000):
    print(i,end=" ")
    count+=1
    if count==5:
        print()
        count=0
        
    