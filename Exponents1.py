# This function asks a user for a base number and an exponent, then calculates the result.

def raise_to_power(base_number, power_number):  # Define a function with two variables
    result = 1  # result is a variable where the math is store. We'll start with it equal to 1
    for index in range(power_number):
        result = result * base_number  # this is what we're doing with the math and it will get stored as the
        # variable "result"

    return result  # We need it to output something, so we use "return" result


base = int(input("What is your base number? "))  # We need to make sure the input is converted to integer
exponent = int(input("What is the exponent you want to raise the base? "))

print(raise_to_power(base, exponent))
