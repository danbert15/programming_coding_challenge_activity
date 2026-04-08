#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

fullname = input("Enter your full name (incorrect casing): ")

reverse_case = fullname.swapcase()

print("Output:", reverse_case)