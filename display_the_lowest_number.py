#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

lowest = None

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        if lowest is None or number < lowest:
            lowest = number
    except ValueError:
        break

if lowest is not None:
    print("The lowest number entered is:", lowest)
else:
    print("No valid numbers were entered.")