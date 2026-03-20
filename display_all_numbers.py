#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

unique_numbers = []

for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

print("Numbers without duplicates:", unique_numbers)