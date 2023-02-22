'''
Validate the user input to see if it is a number
Return a yes or no
'''
def validate_num():
    userNum = input("Please provide a number: ")
    if userNum.isnumeric():
        return "yes"
    else:
        validate_num()

answer = validate_num()
print(answer)
#validate_num()
