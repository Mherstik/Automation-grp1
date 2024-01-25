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
    else:
        position = string.ascii_uppercase.index(each)
        newPos = ((position+shift) % 26)
        #print(position,newPos)
    #    print(string.ascii_uppercase[i], "is pos", i)
    #         if i + shift > 25:
    #             j = i
    #             i = (i + shift) % 26
        print(string.ascii_uppercase[position], "is now", newPos, string.ascii_uppercase[newPos])
        b.append(string.ascii_uppercase[newPos])
#         else:
#             print(string.ascii_uppercase[i], "is now", i+shift, string.ascii_uppercase[i+shift])
#     #else:
#     #    continue

#     i += 1
print(b)

## Convert back to string
str1 = ''
for each in b:
    str1 += each
print(str1)
    
    