import string

# print(string.ascii_letters)
# print(string.ascii_letters[12])
# 
# print(string.ascii_uppercase)
#print(string.printable)

a = input("Give me some letters: ")
a = a.upper()
print(a)
b = []
i = 0
#print(a)
# remove any non-letters except .
for each in a:
    if each == ".":
        b.append("X")
    if each not in string.ascii_uppercase:
        continue
    else:
       b.append(each)
        
    #for each in string.ascii_uppercase:
    #print(string.ascii_uppercase[i], "is pos", i)
#     for letter in a:
#         if letter == string.ascii_uppercase[i]:
#             print(string.ascii_uppercase[i], "is pos", i)
#         else:
#             continue
#     i += 1
        
print("List is", b)

## Convert back to string
str1 = ''
for each in b:
    str1 += each
    
print("string is", str1)


