#function helps us to calculate the factorial of a number

def factorial_loop(r):
    #sets the default value as 1
    result = 1
    #multiplies the values between 1 and the next number after the given number
    for i in range(1,r+2):
        result *= i
    return result

#example case use of the factorial function using the number 20
print(factorial_loop(20))