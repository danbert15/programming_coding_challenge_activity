#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

def my_swapcase(text):
    result = ""

    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch

    return result

string = input("Enter a string: ")
swapped = my_swapcase(string)

print("Result:", swapped)