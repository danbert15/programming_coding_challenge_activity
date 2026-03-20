#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

start = min(number1, number2) + 1
end = max(number1, number2)

for i in range(start, end):
    print(i)