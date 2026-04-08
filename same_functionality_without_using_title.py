#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

text = input("Enter a string: ")

result = ""

new_word = True

for char in text:
    if char.isalpha():
        if new_word:
            result += char.upper()
            new_word = False
        else:
            result += char.lower()
    else:
        result += char
        new_word = True

print("Title-cased string:", result)