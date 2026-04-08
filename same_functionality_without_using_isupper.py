#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

def custom_isupper(text):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

    has_letter = False

    for character in text:
        index = 0

        while index < len(lowercase_letters):
            if character == lowercase_letters[index]:
                return False
            index += 1

        index = 0
        while index < len(uppercase_letters):
            if character == uppercase_letters[index]:
                has_letter = True
                break
            index += 1

    return has_letter

user_input = input("Enter a string: ")
result = custom_isupper(user_input)

print("Result:", result)