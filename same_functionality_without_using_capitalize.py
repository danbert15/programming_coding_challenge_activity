#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

def my_capitalize(text):
    if len(text) == 0:
        return text

    first_char = text[0]
    rest = text[1:]

    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)
    elif 'A' <= first_char <= 'Z':
        first_char = first_char

    new_rest = ""
    for ch in rest:
        if 'A' <= ch <= 'Z':
            new_rest += chr(ord(ch) + 32)
        else:
            new_rest += ch

    return first_char + new_rest

string = input("Enter a string: ")
capitalized = my_capitalize(string)
print("Result:", capitalized)