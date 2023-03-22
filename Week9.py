'''
Name: Port Scanner
Description: Get a list of ports from a user, and an IP address to scan
Input: an IP address, port numbers
Output: open ports
Version: 0.1
Author: Me 
'''
import socket

## Get an IP from a user
# 4 numbers must be between 1-255
## get IP and split on . and check each number

# print(listIPAdd)
# def numTest(ip):
#     for num in ip:
#         try:
#             if not (num.isdigit() and int(num) >= 0 and int(num) <= 255):
#                 raise ValueError
#                 #break
#                 #exit
#         except ValueError:    
#             print("Invalid input. Please enter a valid IP address")
#             

def isValidIPAddress(ip_address_str):
    # Split the IP address into its components
    ip_components = ip_address_str.split(".")

    # Check that the IP address has 4 components
    if len(ip_components) != 4:
        return False
    else:
        # Check that each component is a valid integer between 0 and 255
        for component in ip_components:
            try:
                value = int(component)
                if value < 0 or value > 255:
                    return False
            except ValueError:
                return False
        else:
            return True

def getIPAddress():
    while True:
        ip_address_str = input("Enter an IP address: ")
        if isValidIPAddress(ip_address_str):
            print("Valid IP address:", ip_address_str)
            return ip_address_str
            #break
        else:
            print("Invalid IP address")
            #ip_address_str = input("Enter an IP address: ")
            #continue

        #getIPAddress()

ipAdd = getIPAddress()
################
#    
# using module ipaddress
#
################
# import ipaddress
# 
# ip_address_str = input("Enter an IP address: ")
# 
# try:
#     ip_address = ipaddress.ip_address(ip_address_str)
#     print("Valid IP address:", ip_address)
# except ValueError:
#     print("Invalid IP address")

#while True:
# for each in ipAdd.split("."):ip_address_str
#     #print(each)
#     if each.isdigit() and int(each) >= 0 and int(each) <= 255:
#         # break
#         continue
#     else:
#         print(each, "it's not a valid number")
#         ipAdd = input("Give me an IP address: ")
#         continue

## Get list of ports
portList = []
# low = 1 high = 65535
print("Give me a port number.\nPress X to exit")
while True:
    port = input("Port: ")
    if port.lower() == "x":
        break
    elif port.isdigit():
        if int(port) > 0 and int(port) <= 65535:
            portList.append(int(port))
        else:
            print("Give me a number between 1 and 65535")
    else:
        print("Give me a valid number")

# print(portList)
# for each in portList:
#     print(type(each))
# print(ipAdd)

### Create a socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in portList:
    try:
        s.connect((ipAdd, port))
        print(f"{ipAdd} at port {port} is open")
    except:
        print(f"{ipAdd} at port {port} is closed")
    #s.close()

