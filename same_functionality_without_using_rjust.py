#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

def custom_rjust(s, total_length):
    num_spaces = total_length - len(s)
    if num_spaces > 0:
        return ' ' * num_spaces + s
    else:
        return s

string_input = input("Enter the string: ")
length_input = int(input("Enter total length: "))

print("Result after rjust:", '"' + custom_rjust(string_input, length_input) + '"')