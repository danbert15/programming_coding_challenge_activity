#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

def custom_lower(text):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for character in text:
        index = 0
        found = False

        while index < len(uppercase):
            if character == uppercase[index]:
                result += lowercase[index]
                found = True
                break
            index += 1

        if not found:
            result += character

    return result

user_input = input("Enter a string: ")
converted_text = custom_lower(user_input)

print("Result:", converted_text)