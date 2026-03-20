#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Check to avoid division by zero
if number2 != 0:
    remainder = number1 % number2
    print("The remainder is:", remainder)
else:
    print("Cannot divide by zero.")