# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:47:41 2024

@author: trankieuvy
"""


n = int(input("Nhập n: "))
dem = 0

for so in range(2, n):
    nguyen_to = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            nguyen_to = False
            break
    if nguyen_to:
        dem += 1

print("Số lượng số nguyên tố nhỏ hơn", n, "là:", dem)