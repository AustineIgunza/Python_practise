#this function helps us  to check whether a number is even or odd
def check_even_or_odd(number):
    #checks if number can be devided by 2 and not leave a reminder
    if number%2==0:
        return "Even"
    else:
        return "Odd"


#example case to check whether 17 is an even or odd number
print(check_even_or_odd(17)) #output will be odd since it leaves a reminder when devided by 2
