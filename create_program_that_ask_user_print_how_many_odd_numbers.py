#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_numbers = []
count = 0

for i in range(10):
    number = int(input("Enter a number: "))

    if number % 2 != 0:
        count = count + 1
        odd_numbers.append(number)

print("The total of odd numbers are:", count)
print("The odd numbers are:", odd_numbers)