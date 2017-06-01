# define the main method of the program
def main():
    # get n from the user to be passed to fibonacci()
    n = eval(input('What number do you want to find in the fibonacci sequence? '))
    # Invoke fibonacci()
    fibonacci(n)
# this method generates the fibonacci sequence up to n given by the user
# and returns the last number of the sequence thus giving the nth fibonacci number
def fibonacci(n):
    fibo = [1]
    a = 0
    b = 1
    for n in range(1, n):
        temp = b + a
        fibo.append(temp)
        a = b
        b = temp
    print('Result:', fibo[-1])
# call the main method and initialize the program
main()