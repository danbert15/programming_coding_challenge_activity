#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

fullname = input("Enter your full name (incorrect casing): ")

snake_case = "_".join(fullname.lower().split())

print("Output:", snake_case)