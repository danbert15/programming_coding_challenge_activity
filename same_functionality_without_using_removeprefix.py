#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

def custom_removeprefix(text, prefix):

    if text[:len(prefix)] == prefix:
        return text[len(prefix):]
    return text

user_input = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")

result = custom_removeprefix(user_input, prefix)

print("Result:", result)