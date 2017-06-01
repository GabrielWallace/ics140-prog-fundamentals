#Prompt user to enter a sentence
sentence = input("Please enter a sentence: ")
#Split the sentence to extract each word
sentence = sentence.split()
#Create an array to hold the values of each word length
lenOfWordArray = []
#Iterate over sentence and append the length of each word to lenOfWordArray
for word in sentence:
    lenOfWordArray.append(len(word))
#Average variable
average = sum(lenOfWordArray) // len(lenOfWordArray)
#Display the average word length of the sentence
print("The average word length in your sentence is",average,"characters")