#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

statement = input("Enter a complete statement: ")

words = statement.split()

word_count = len(words)

print("Number of words:", word_count)