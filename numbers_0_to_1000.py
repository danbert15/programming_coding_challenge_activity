#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

number = int(input("Enter a number (0-1000): "))

formatted = str(number).zfill(6)

print("Output:", formatted)