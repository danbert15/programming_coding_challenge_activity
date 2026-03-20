#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 < number2:
    print("The smallest number is: ", number1)
elif number2 < number1:
    print("The smallest number is: ", number2)
else:
    print("Both numbers are equal")