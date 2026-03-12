#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total = 0

for i in range(10):
    number = float(input("Enter a number: "))
    total = total + number

print("The total sum of the two numbers is", total)