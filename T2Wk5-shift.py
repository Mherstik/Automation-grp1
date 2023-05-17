import string

i = 0
a = input("Give me the plain text: ")
shift = int(input("Tell me the key: "))
shift = shift % 26

a = a.upper()
b = []
for each in string.ascii_uppercase:
    #print(string.ascii_uppercase[i], "is pos", i)
    if each == ".":
      b.append("X")
    for letter in a:
        if letter == string.ascii_uppercase[i]:
            print(string.ascii_uppercase[i], "is pos", i)
            if i + shift > 25:
                i = (i + shift) % 26
                print(string.ascii_uppercase[i], "is now", i, string.ascii_uppercase[i])
            else:
                print(string.ascii_uppercase[i], "is now", i+shift, string.ascii_uppercase[i+shift])
        else:
            continue
    i += 1