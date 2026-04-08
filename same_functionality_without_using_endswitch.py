#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

def custom_endswith(text, suffix):
    text_length = len(text)
    suffix_length = len(suffix)

    if suffix_length > text_length:
        return False

    index = 0
    while index < suffix_length:
        if text[text_length - suffix_length + index] != suffix[index]:
            return False
        index += 1

    return True

user_input = input("Enter a string: ")
suffix = input("Enter suffix to check: ")

result = custom_endswith(user_input, suffix)

print("Result:", result)