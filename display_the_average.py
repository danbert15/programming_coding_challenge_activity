#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

if numbers:
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("No valid numbers were entered.")