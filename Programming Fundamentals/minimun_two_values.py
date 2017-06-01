def main():
    num1 = eval(input('Please enter a number(num1): '))
    num2 = eval(input('Please enter a number(num2): '))
    print(minVal(num1, num2))

def minVal(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
main()