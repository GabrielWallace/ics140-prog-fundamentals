numsToAdd = eval(input("How many numbers will you be adding?  "))
numbers = []
iteration = 0
for x in range(numsToAdd):
    iteration +=1
    print("Entry", iteration, "of", numsToAdd)
    numbers.append(eval(input("Please enter a number: ")))
results = sum(numbers)
print("\nThe sum of", numbers," = ", results)