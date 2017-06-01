# The main method that initializes the program and gets the user input and invokes
# all needed methods
def main():
    print('This program takes an integer as input and generates the first n natural numbers')
    nth = eval(input('How many natural numbers do you want to generate? '))
    # create a list of the natural numbers
    n = [x for x in range(1, nth + 1)]
    # invoke _sum()
    _sum(n)
    # invoke sumNCubes()
    sumNCubes(n)
# This method takes the list of natural numbers and adds them
def _sum(n):
    sumN = 0
    for num in range(len(n)+1):
        sumN += num
    print('The sum of', n, 'is', sumN)
# This method takes the list of natural numbers, finds their cubes and adds them
def sumNCubes(n):
    squares = [x**3 for x in n]
    print('\nThe sum of',squares, 'is', sum(squares))
# Invoke main() and initialize the program
main()