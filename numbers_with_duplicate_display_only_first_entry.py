#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

seen = []

print("Numbers (duplicates shown only once):")
for num in numbers:
    if num not in seen:
        print(num)
        seen.append(num)