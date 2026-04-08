#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

fullname = input("Enter your full name (incorrect casing): ")

proper_name = fullname.title()

print("Output:", proper_name)