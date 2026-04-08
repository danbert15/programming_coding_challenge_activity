#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

def is_all_lower(s):
    if not s:
        return False
    for char in s:
        if char.isalpha() and not ('a' <= char <= 'z'):
            return False
    for char in s:
        if char.isalpha():
            return True
    return False

user_input = input("Enter a string: ")

if is_all_lower(user_input):
    print("All alphabetic characters are lowercase.")
else:
    print("Not all alphabetic characters are lowercase.")