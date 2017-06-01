import math

def factorial():
    num = eval(input("Please enter a number: "))
    print(math.factorial(num))

def divide_two_numbers():
    num1 = eval(input("Please enter a number 1: "))
    num2 = eval(input("Please enter a number 2: "))
    print(num1/num2)

try:
    factorial()
except ValueError as e:
    print("No negative integers allowed", e)

try:
    divide_two_numbers()
except ZeroDivisionError as e:
    print("Division by zero not allowed!", e)