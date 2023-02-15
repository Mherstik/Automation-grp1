'''
Description: A program to help make beverages
Author: Marcus + Cyber Grp 1
Date: 15/Feb/2023
Ask user for beverage choice and milk/sugar
'''

import time

# Ask user for their name

cust_Name = input("What is your name: ")

# Ask if they want a beverage

bev_Question = input("Hi " + cust_Name +" would you like a beverage [y/n]: ")
bev_Question = bev_Question.lower()
#print(bev_Question)

while not (bev_Question == "y" or bev_Question == "yes" or bev_Question == "no" or bev_Question == "n"):
    print("Please choose yes or no")
    bev_Question = input("Would you like a beverage [y/n]: ").lower()

if bev_Question == "n" or bev_Question == "no":
    print("Sorry to her that. \r\n Goodbye")
    exit()

# Ask for beverage type
# Options: Tea, Coffee
bev_Choice = input("Choose from coffee or tea: ").lower()
bev_List = ["tea", "coffee", 't', 'c' ]

while bev_Choice not in bev_List:
    bev_Choice = input("Choose from coffee or tea: ").lower()

milk_List = ["full cream", 'f', "lactose free", "lf", "almond", "a", "soy", "s", "oat", "o" ]


## Ask if they want milk
milk_question = input("Would you like milk [y/n]: ").lower()
if milk_question == "yes" or milk_question == "y":
    #milk_choice = input("Please choose a milk. \r\nChoices are: full cream (f), lactose free (lf), almond (a), soy (s), oat, (o)")  
    milk_choice = input("Please choose a milk. \r\nChoices are:" + str(milk_List))  
    while milk_choice not in milk_List:
        milk_choice = input("Please choose a milk. \r\nChoices are: full cream (f), lactose free (lf), almond (a), soy (s), oat, (o)")  

# Ask how much sugar

print("here is your beverage")

