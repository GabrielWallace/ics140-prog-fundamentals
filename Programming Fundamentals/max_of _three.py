def design_one():
    x1 = eval(input("Please input the first number: "))
    x2 = eval(input("Please input the second number: "))
    x3 = eval(input("Please input the third number: "))

    if x1 >= x2 >= x3:
        print("Max is ", x1)
    elif x2 >= x1 >= x3:
        print("Max is ", x2)
    else:
        print("Max is ", x3)

def design_two():
    x1 = eval(input("Please input the first number: "))
    x2 = eval(input("Please input the second number: "))
    x3 = eval(input("Please input the third number: "))

    if x1 >= x2:
        if x1 >= x3:
            print("Max is", x1)
        else:
            print("Max is", x3)
    elif x1 < x2:
        if x2 >= x3:
            print("Max is", x2)
        else:
            print("Max is", x3)

def design_three():
    x1 = eval(input("Please input the first number: "))
    x2 = eval(input("Please input the second number: "))
    x3 = eval(input("Please input the third number: "))
    maxnum = x1
    if x2 >= maxnum:
        maxnum = x2
    if x3 >= maxnum:
        maxnum = x3
    print(maxnum)

design_three()