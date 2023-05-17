# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:35:42 2023

@author: Marcus
"""

import string

i = 0
a = input("Give me the plain text: ")
shift = int(input("Tell me the key: "))
shift = shift % 26

a = a.upper()
b = []
j = ''
# for each in string.ascii_uppercase:
for each in a:
    #print(string.ascii_uppercase[i], "is pos", i)
    if each == ".":
      b.append("X")
    position = string.ascii_uppercase.index(each)
    newPos = position+shift
    print(position,newPos)
#         print(string.ascii_uppercase[i], "is pos", i)
#         if i + shift > 25:
#             j = i
#             i = (i + shift) % 26
#             print(string.ascii_uppercase[j], "is now", i, string.ascii_uppercase[i])
#         else:
#             print(string.ascii_uppercase[i], "is now", i+shift, string.ascii_uppercase[i+shift])
#     #else:
#     #    continue
#     i += 1
