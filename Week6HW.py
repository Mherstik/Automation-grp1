
### Program that gets a random number from 1 - 100
## We guess and the program says high or low
## We get 5 guesses

import random

# print a random number from 1 - 100
a = random.randrange(100)
print(a)
# get a number from the user
b = input("Give me a number: ")
try:
    int(b)
    b = int(b)
except:
    print("You need to give a number")

if a == b:
    print("You got it")
else:
    print("BOOO!!!")




