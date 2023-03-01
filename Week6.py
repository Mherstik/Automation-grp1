"""
Description: IP address creator
Get 4 numbers from a user to create an IP address.
Author: MH
Date: 1/3/2023
Version: 0.1
"""
ipAdd = []
def ipGenerator():
    userNum = input("Give me a number: ")
    #userNum = int(userNum)
    # check it is a valid number
    attempt = 1
    check = False
    while check == False and attempt < 3:
        if userNum.isdigit() and float(userNum) <= 255:
            ipAdd.append(userNum)
            check = True 
        else:
            print("I need a number from 0 and 255.")
            userNum = input("Give me a number: ")
            attempt = attempt + 1
            if attempt == 3:
                print("Too many attempts")
                #exit("Error: Too many attempts")
    
for i in range(4):
    ipGenerator()

#print(ipAdd)

try:
    #print(ipAdd[0],ipAdd[1],ipAdd[2],ipAdd[3],sep=".")
# #except:
# #    print("Error: Not enough numbers")
# 
except IndexError:
   print("Index Out of Bound.")

