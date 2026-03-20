#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number2 != 0:
    quotient = number1 // number2
    print("The quotient is:", quotient)
else:
    print("Cannot divide by zero.")