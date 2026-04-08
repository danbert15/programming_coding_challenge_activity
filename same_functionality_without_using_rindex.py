#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

def custom_rindex(s, sub):
    sub_len = len(sub)
    # Loop from the end of the string backwards
    for i in range(len(s) - sub_len, -1, -1):
        if s[i:i+sub_len] == sub:
            return i
    raise ValueError(f"substring '{sub}' not found in '{s}'")

string_input = input("Enter the string: ")
substring_input = input("Enter the substring to find from the end: ")

try:
    position = custom_rindex(string_input, substring_input)
    print(f"The substring last appears at index {position}.")
except ValueError as egg: #from 'e' to 'egg'
    print(egg)