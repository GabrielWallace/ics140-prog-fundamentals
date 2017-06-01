#Prompt the user to enter their name
name = input("Please enter your name(one name only): ")
#Convert the sentence to all lower case to allow the ord() function to work correctly since
#Capital letters will have a different value than lowercase ones
name = name.lower()
#Put all the characters from the name into an array
chars = [char for char in name]
#Iterate over chars[] and return the ord() value - 96 for each character and put the values
#into an array
numbers = [ord(c)-96 for c in name]
#Sum the values of numbers[]
sumOfName = sum(numbers)
#Display results
print("You're name =", sumOfName)