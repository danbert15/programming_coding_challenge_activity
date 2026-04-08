#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

def starts_with(s, prefix):
    prefix_len = len(prefix)
    if s[:prefix_len] == prefix:
        return True
    else:
        return False

string_input = input("Enter the string: ")
prefix_input = input("Enter the prefix to check: ")

if starts_with(string_input, prefix_input):
    print("The string starts with the prefix.")
else:
    print("The string does not start with the prefix.")