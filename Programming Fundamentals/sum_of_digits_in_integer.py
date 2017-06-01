def main():
    number = eval(input("Please enter a number: "))
    sumDigits(number)

def sumDigits(n):
    digit_list = [int(x) for x in str(n)]
    print(digit_list)
    print(sum(digit_list))

main()