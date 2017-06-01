def day_of_week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    user_input = eval(input("Please enter the day of the week as an integer (Monday = 1): "))
    if user_input <= 0 or user_input > 7:
        print("Value out of range, please enter a number between 1 and 7.  Please try again")
        day_of_week()
    if user_input == 1:
        print("Day of the week: ",days[0])
    elif user_input == 2:
        print("Day of the week: ",days[1])
    elif user_input == 3:
        print("Day of the week: ",days[2])
    elif user_input == 4:
        print("Day of the week: ",days[3])
    elif user_input == 5:
        print("Day of the week: ",days[4])
    elif user_input == 6:
        print("Day of the week: ",days[5])
    elif user_input == 7:
        print("Day of the week: ",days[6])
day_of_week()