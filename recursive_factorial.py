#function to give us the recursive factorial of a given number

def recursive_factorial(r):
    if r ==0 or r==1:
        return 1
    else:
        return r*recursive_factorial(r-1)

#example use to get the recursive factorial of the number 16
print(recursive_factorial(16))