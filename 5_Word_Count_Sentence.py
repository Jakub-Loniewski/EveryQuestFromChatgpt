#Write a program that asks the user to enter a sentence and then counts the number of words in that sentence.
#The program should ignore extra spaces between words.

#Ask user to enter a sentence
sentence = input("Put some sentence")
#Remove extra spaces at the beginning and end, then split the sentence into words
words = sentence.strip().split()
#Count the words
word_count = len(words)
#Display the result
print(f"The number of words in your sentence is: {word_count}")