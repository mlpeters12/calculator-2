"""
calculator.py

Using our arithmetic.py file from Euser_entryercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
math_functions = ['+', '-', '*', '/', '%', '**2', "**3", "**" ]
user_entry = raw_input("Please type an arithmetic function followed by 2 numbers. ")
# Your code goes here
while True:

    response = user_entry.split(" ")
    num1 = int(response[1])
    num2 = int(response[2])

    if response[0] == "q" or response[0]== "Q":
        break
    elif response[0] in math_functions:
            if response[0] =="+":
                result = add(num1, num2)
            elif response[0] =="-":
                result = subtract(num1, num2)
            elif response[0] =="*":
                result = multiply(num1,num2)
            elif response[0] =="/":
                result = divide(num1, num2)
            elif response[0] =="%":
                result = mod(num1,num2)
            elif response[0] =="**2":
                result = square(num1)
            elif response[0] =="**3":
                result = cube(num1)
            elif response[0] =="**":
                result = power(num1, num2)
            print "The answer is %.2f" %(result)
            break
    else:
        print "You didn't pick a valid math function."
        break