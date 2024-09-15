# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:54:35 2024

@author: Admin
"""

tongchan=0
tongle=0
for i in range(101):
    if i%2==0:
        tongchan+=i
    else:
        tongle+=i
print("Tổng các số chẵn từ 0 đến 100 là:",tongchan)
print("Tổng các số lẽ từ 0 đến 100 là:",tongle)
