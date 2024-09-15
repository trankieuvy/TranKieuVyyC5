# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:29:13 2024

@author: trankieuvy
"""

chuoi = input("Nhập một chuỗi: ")

length = len(chuoi)
print("Độ dài chuỗi: ", length)

kydb = "!@#$%^&*()-=+./"
dem_kydb = 0
for i in chuoi:
    if i in kydb:
        dem_kydb += 1
print("Số ký tự đặc biệt: ", dem_kydb)

dem_thuong = 0
for i in chuoi:
    if i.islower():
        dem_thuong += 1
print("Số ký tự chữ cái thường [a-z]: ", dem_thuong)

dem_so = 0
for i in chuoi:
    if i.isdigit():
        dem_so += 1
print("Số ký tự chữ số [0-9]: ", dem_so)

dem_hoa = 0
for i in chuoi:
    if i.isupper():
        dem_hoa += 1
print("Số ký tự chữ cái hoa [A-Z]: ", dem_hoa)
