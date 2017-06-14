#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/6/14 20:12
@Author  : Mr.Sprint
@File    : test.py
@Software: PyCharm
'''
import binascii
str1 = '0x67'
str2 = hex(eval(str1))
print(chr(int(str2,16)))
with open('b.bin','w') as f:
    f.write(chr(int(str2,16)))

