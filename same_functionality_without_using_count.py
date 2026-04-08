#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

def custom_count(s, sub):
    count = 0
    sub_len = len(sub)

    for i in range(len(s) - sub_len + 1):

        if s[i:i + sub_len] == sub:
            count += 1
    return count

string_input = input("Enter the string: ")
substring_input = input("Enter the substring to count: ")

print(f'The substring appears {custom_count(string_input, substring_input)} times.')