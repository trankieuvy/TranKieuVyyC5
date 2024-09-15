# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:51:33 2024

@author: Admin
"""

import random
a= random.randint(1,11)
print("Số lượng phần tử ngẫu nhiên: ",a)
for i in range(a):
    b=random.randint(20,31)
    print(b)
    
import random 
soluongphantu=random.randint(1,82)
print("Số lượng pt được chọn ngẫu nhiên là: ",soluongphantu)
binhphuong=[]
for songaunhien in range(soluongphantu):
    songaunhien=random.uniform(18, 99)
    binhphuong.append(songaunhien**2)
print("Ds các giá trị bình phương: ",binhphuong)
