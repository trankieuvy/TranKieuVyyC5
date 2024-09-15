# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:30:08 2024

@author: Admin
"""
#1.tạo danh sách các số chia hết cho 9
print("danh sách các số chẵn nguyên chia hết cho 9:")
i=[]
for i in range(2020,3838):
    if i % 2==0 and i%9==0:
      
        print(i)
        
#2.số thu được thành chuỗi trên một dòng, cách nhau bằng 1 tab
print("danh sách các số chẵn nguyên chia hết cho 9:")
i=[]
for i in range(2020,3838):
    if i % 2==0 and i%9==0:
      
        print(i,end='\t')
        