def eligibility_check():
    age = eval(input("Please enter your age: "))
    years = eval(input("Please enter the length of your citizenship in years: "))
    if age >= 30 and years >= 9:
        print("You are eligible for Senatorship")
    else:
        print("You are NOT eligible for Senatorship")

    if age >= 25 and years >= 7:
        print("You are eligible to be a Representative")
    else:
        print("Not eligible for rep")

eligibility_check()