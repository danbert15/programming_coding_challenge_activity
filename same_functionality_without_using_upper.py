#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char
    return result

user_input = input("Enter a string: ")
print("Uppercase version:", to_uppercase(user_input))