#this function will take the digits of a given number and sum them and give the sum of the digits as output

def sum_of_number_digits(number):
    #sets the default value of the total as 0
    total = 0
    while number >0:
        digit = number % 10
        total += digit
        number //=10
    return total


#example case use that sums the digits of the number 4567 and prints the sum
print(sum_of_number_digits(4567))