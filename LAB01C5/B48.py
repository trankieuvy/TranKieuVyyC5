# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:19:46 2024

@author: trankieuvy
"""

tongnhonhat = 10**9
bonghiem = 0

for z in range(1, 979 // 9 + 1):
    for y in range(1, (979 - 9 * z) // 7 + 1):
        conlai = 979 - 9 * z - 7 * y
        if conlai > 0 and conlai % 2 == 0:
            x = conlai // 2
            tong = x + y + z
            if tong < tongnhonhat:
                tongnhonhat = tong
                bonghiem = (x, y, z)

if bonghiem:
    print(f"Bộ nghiệm có tổng x + y + z nhỏ nhất là: x = {bonghiem[0]}, y = {bonghiem[1]}, z = {bonghiem[2]}")
else:
    print("Không có bộ nghiệm nào thỏa mãn.")
