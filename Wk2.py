'''
Description: Class- Automation Grp 1
Date: Week 2 
Author: Marcus Herstik

Notes: Must be in class

'''
#print(2 + 2)
# var1 = "Marcus"
# var2 = "Herstik"
#
#type()
# print(var1,var2)
# print(var1 + var2)

# firstName = input()
# print(firstName)
#print(input("What is your name: ")
name = input("What is your name: ")

## say hello name
print("Hello", name)

## ask for names age and store as age
#age = int(input("How old are you: "))
###
#
# # if the age type is int = OK
# if type(age) is not str:
#     print("This is not a string")
# # else ask for age again
# elif type(age) is str:
#     print("This is a string")
#     if type(int(age)) is int:
#         print("This did work")
#     else:
#         print("They didn't put a number")
# #####
# else:
#     print("Congratulations, you are 18")
# 
# 
# print("Hello", name, "you are", age, "years old")

## Tell them how old they will be next year
#print("Next year you will be", age + 1)

attempt = 0
age = input("How old are you: ")
while not age.isdigit():
    print("attempt = ", attempt)
    attempt = attempt +  1
    print("attempt = ", attempt)
    print("Please use a whole number!")
    age = input("How old are you: ")
    if attempt == 3:
        print("Try again later")
        age = 0
        break
    
# convert age to integer
age = int(age)






