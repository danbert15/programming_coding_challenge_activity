#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

fullname = input("Enter your full name (incorrect casing): ")

words = fullname.split()
pascal_case = ""

for word in words:
    pascal_case += word.capitalize()

print("Output:", pascal_case)