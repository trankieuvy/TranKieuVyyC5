# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:44:29 2024

@author: Admin
"""

import random

sove = int(input("Nhập số vé bạn muốn mua: "))
tongtienthang = 0
giave = 10000

sotrungthuong = []
while len(sotrungthuong) < 6:
    so = random.randint(1, 45)
    if so not in sotrungthuong:
        sotrungthuong.append(so)
sotrungthuong.sort()
print("Dãy số trúng thưởng: ", sotrungthuong)

for i in range(sove):
    ve = []
    while len(ve) < 6:
        so = random.randint(1, 45)
        if so not in ve:
            ve.append(so)
    ve.sort()
    
    sotrung = 0
    for num in ve:
        if num in sotrungthuong:
            sotrung += 1

    if sotrung == 6:
        tongtienthang += 10000000000
    elif sotrung == 5:
        tongtienthang += 10000000
    elif sotrung == 4:
        tongtienthang += 300000
    elif sotrung == 3:
        tongtienthang += 30000

    print("Vé", i + 1, ":", ve, "- Trùng", sotrung, "số, Thưởng:", "{:,}".format(tongtienthang), "vnđ")

tongchiphi = sove * giave
print("Tổng tiền trúng:", "{:,}".format(tongtienthang), "vnđ")
print("Tổng chi phí:", "{:,}".format(tongchiphi), "vnđ")
print("Lợi nhuận:", "{:,}".format(tongtienthang - tongchiphi), "vnđ")

 


