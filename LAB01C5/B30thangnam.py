# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:39:01 2024

@author: trankieuvy
"""

mm=int(input("Nhập vào tháng: "))
yy=int(input("Nhập vào năm: "))
while  mm<1 and mm>12 and yy<0:
    print("Tháng năm nhập vào không hợp lệ. Vui lòng nhập lại.")
else:
    if mm==2:
        if yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
            dd=29
        else:
            dd=28
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
            dd=30
    else:
            dd=31
print("Tháng",mm,"năm",yy, "có",dd,"ngày")
    
    
    
    
        