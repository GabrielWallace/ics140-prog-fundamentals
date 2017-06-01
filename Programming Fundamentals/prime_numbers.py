def main():
    number = eval(input('Please enter a number: '))
    prime_check(number)


def prime_check(num):
    if num >= 2:
        for y in range(2, num):
            if not (num % y):
                print('not prime')
    else:
        print('not prime')
    print('is prime')

main()