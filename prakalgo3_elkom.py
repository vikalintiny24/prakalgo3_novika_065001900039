# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 01:31:39 2021

@author: vikal
"""

kecil = int(input("Masukkan angka pertama : "))
besar = int(input("Masukkan angka terkahir : "))

while kecil and kecil <= besar:
    print(kecil, besar)
    kecil += 1
    besar -= 1


