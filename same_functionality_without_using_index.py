#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

def custom_index(s, sub):
    sub_len = len(sub)
    for i in range(len(s) - sub_len + 1):
        if s[i:i+sub_len] == sub:
            return i
    raise ValueError(f"substring '{sub}' not found in '{s}'")

string_input = input("Enter the string: ")
substring_input = input("Enter the substring to find: ")

try:
    position = custom_index(string_input, substring_input)
    print(f"The substring first appears at index {position}.")
except ValueError as egg: #I changed the 'e' to "egg"
    print(egg)