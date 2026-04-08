#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

def custom_lstrip(text):
    index = 0

    while index < len(text) and text[index] == ' ':
        index += 1

    return text[index:]

user_input = input("Enter a string: ")
result = custom_lstrip(user_input)

print("Result:", result)