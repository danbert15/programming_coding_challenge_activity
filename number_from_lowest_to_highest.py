#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

if numbers:
    numbers.sort()
    print("Numbers from lowest to highest:", numbers)
else:
    print("No valid numbers were entered.")