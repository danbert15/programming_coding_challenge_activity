#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid.
#Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

numbers = []

while True:
    user_input = input("Enter a number (or any non-number to stop): ")
    if not user_input.isdigit():
        print("Invalid input. Stopping program.")
        break

    num = int(user_input)

    if num in numbers:
        print(f"{num} - Duplicate")
    else:
        print(f"{num} - Unique")
        numbers.append(num)