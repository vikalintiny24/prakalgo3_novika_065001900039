# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 01:29:24 2021

@author: vikal
"""

total = int(input("Masukkan total belanjaan :  "))
bayar = int(input("Masukkan jumlah uang Anda:  "))
kembalian = bayar - total
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
sisa = kembalian

print("\nKembalian yang diberikan: ", kembalian, "\nPecahan uang yang diberikan: ")
for pecahan in uang_pecahan:
    if sisa < pecahan:
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - (pecahan * banyak_pecahan)
    print("Uang kertas {} sebanyak {} lembar".format(pecahan, banyak_pecahan))