# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:56:15 2024

@author: Admin
"""
print("Kết quả: ")
j = 0
for i in range(0, 10):
    j += i
    print(j)
"""
# print("Kết quả: ")
    0
    1
    3
    6
    10
    15
    21
    28
    36
    45
"""

print("Kết quả: ")
j = 1
for i in range(0, 10):
     j += j
     print(j)
"""
Kết quả: 
1024
"""
print("Kết quả: ")
for j in range(0, 10):
      j += j
      print("j")
      