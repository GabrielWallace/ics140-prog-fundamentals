#Counter variable to increment for each test score to make it easier on the user
counter = 0
#Get the amount of scores the user will be entering
numberOfScores = int(input("How many different scores will you be entering? "))
#Create an array of the test scores
scores = []
#Loop through the score input for the amount in numberOfScores
for x in range(numberOfScores):
    #Increment counter
    counter += 1
    #Print counter
    print("Test #", counter)
    #Get score input
    scores.append(float(input("Please enter the score for test: ")))
#Add the values in the scores array
scoresTotal = sum(scores)
#Calculate the average score
average = scoresTotal / numberOfScores
#Print the average score
print(average)