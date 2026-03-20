#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

if numbers:
    numbers.sort(reverse=True)
    print("Numbers from highest to lowest:", numbers)
else:
    print("No valid numbers were entered.")