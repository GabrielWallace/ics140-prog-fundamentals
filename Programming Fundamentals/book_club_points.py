def main():
    books = eval(input('Please enter the total number of books you bought this month: '))
    calculate_points(books)


def calculate_points(n):
    points = 0
    if n == 0:
        points = 0
    elif n == 2:\
        points = 5
    elif n == 4:
        points = 15
    elif n == 6:
        points = 30
    elif n >= 8:
        points = 60
    print(points)

main()