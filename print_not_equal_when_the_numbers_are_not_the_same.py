#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 != number2:
    print("Not equal")
else:
    print("Equal")