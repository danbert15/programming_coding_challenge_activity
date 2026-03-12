#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
    print("The first number is bigger:", number1)
elif number2 > number1:
    print("The second number is bigger:", number2)
else:
    print("Both numbers are the same")