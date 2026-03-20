#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

numbers = []

for i in range(10):
    num = input(f"Enter number {i+1}: ")
    numbers.append(num)

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

if duplicates:
    print("Numbers with duplicates:", duplicates)
else:
    print("No duplicates found.")