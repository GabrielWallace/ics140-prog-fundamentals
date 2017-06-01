def validate_date():
    # Get the date input from the user
    date = input("Enter a date in mm/dd/yyyy format (12/25/2017): ")
    # Split the input at occurrences of "/"
    split_date = date.split("/")
    # Isolate the value that represents the month
    month = eval(split_date[0])
    # Isolate the value that represents the day
    day = eval(split_date[1])
    ## I left out year since that does not seem to matter within the scope of this assignment.##

    # Check February for proper day input
    if month == 2:
        if day > 29:
            print(date, "Invalid date")
        else:
            print(date, "Valid date")
    # Check April, June, September, and November for proper day input
    elif month in (4, 6, 9, 11):
        if day > 30:
            print(date, "Invalid date")
        else:
            print(date, "Valid date")
    # Check Jan, Mar, May, Jul, Aug, Oct, Dec for proper day input
    elif month in (1, 3, 5, 7, 8, 10, 12):
        if day > 31:
            print(date, "Invalid date")
        else:
            print(date, "Valid date")
validate_date()
