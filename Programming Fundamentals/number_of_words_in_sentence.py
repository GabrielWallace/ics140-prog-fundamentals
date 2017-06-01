#Prompt the user to enter the message
message = input("Please enter your message: ")
#Split the message at its whitespace and count the words
wordCount = len(message.split())
#Print the total word count in the message
print(wordCount)