#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

def custom_ljust(text, total_length):
    text_length = len(text)

    if text_length >= total_length:
        return text

    result = text

    while len(result) < total_length:
        result += " "

    return result

user_input = input("Enter a string: ")
desired_length = int(input("Enter total length: "))

output = custom_ljust(user_input, desired_length)

print("Result: '" + output + "'")