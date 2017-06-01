def age_classifier():
    age = eval(input("Please enter your age (30): "))

    if age < 0:
        print("Negative ages do not exist.  Please try again.")
        age_classifier()
    elif age <= 1:
        print("You are an infant")
    elif age > 1 and age < 13:
        print("You are a child")
    elif age >= 13 and age < 20:
        print("You are a teenager")
    else:
        print("You are an adult")
age_classifier()