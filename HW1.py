import random
import pyinputplus as pyip


print("       !!!GUSSING GAME!!!")
print("Enter your preferred heighest range :", end=" ")
randomRange = pyip.inputNum()
randomNumber = random.randint(0,randomRange)
attampt = 1

while attampt <= 5:

    print("Guess a value between 0 to", randomRange, end=": ")
    userInput = pyip.inputNum()

    #print(randomNumber)
    if userInput == randomNumber:
        print("Great Job!!!, You gussed the number ", randomNumber)
        print("You only took", attampt, "gusses")
        exit()
    elif userInput < randomNumber:
        print("your guess is LOWER")
    else:
        print("your guess is HIGHER")
        
    attampt = attampt + 1
    

print("Random Value is ", randomNumber)
print("Goodluck next time!!!")