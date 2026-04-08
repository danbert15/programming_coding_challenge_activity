#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

fullname = input("Enter your full name (with spaces at the beginning): ")

clean_name = fullname.lstrip()

print("Output:", clean_name)