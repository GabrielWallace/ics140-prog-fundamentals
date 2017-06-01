"""
dayNum = 31(month – 1) + day

if the month is after February subtract (4(month) + 32)//10

if it’s a leap year and after February 29, add 1
"""


def convert_date():
    date = [int(num) for num in input('Enter the date in month/day/year (06/28/1986) format: ').split('/')]

    month, day, year = abs(date[0]), abs(date[1]), abs(date[2])

    if not validate_date(date):
        print('Invalid date.  Try again.')
        convert_date()

    day_num = (31 * (month - 1)) + day
    after_feb = ((4 * month) + 32) // 10

    if leap_check(year) and month > 2:
        day_num = day_num - after_feb + 1
        print(day_num, '0')

    elif not leap_check(year) and month > 2:
        day_num -= after_feb
        print(day_num, '1')

    else:
        print(day_num, '2')


def leap_check(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def validate_date(lst):
    month, day, year = lst[0], lst[1], lst[2]
    # Check February for proper day input
    if month < 1 or day < 1 or year < 1:
        return False
    elif month == 2:
        if day > 29 and not leap_check(year):
            return False
        else:
            return True
    # Check April, June, September, and November for proper day input
    elif month in (4, 6, 9, 11):
        if day > 30:
            return False
        else:
            return True
    # Check Jan, Mar, May, Jul, Aug, Oct, Dec for proper day input
    elif month in (1, 3, 5, 7, 8, 10, 12):
        if day > 31:
            return False
        else:
            return True


if __name__ == '__main__':
    convert_date()
