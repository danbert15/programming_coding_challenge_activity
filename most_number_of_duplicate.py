#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

if numbers:
    max_count = 0
    most_duplicate = None

    for number in numbers:
        count = numbers.count(number)
        if count > max_count:
            max_count = count
            most_duplicate = number

    if max_count > 1:
        print("Number with most duplicates:", most_duplicate)
        print("Number of occurrences:", max_count)
    else:
        print("No duplicates found.")
else:
    print("No valid numbers were entered.")