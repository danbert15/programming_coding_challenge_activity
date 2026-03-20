#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

highest = None

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        if highest is None or number > highest:
            highest = number
    except ValueError:
        break

if highest is not None:
    print("The highest number entered is:", highest)
else:
    print("No valid numbers were entered.")