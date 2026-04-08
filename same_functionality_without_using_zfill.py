#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

def custom_zfill(s, total_length):
    num_zeros = total_length - len(s)
    if num_zeros > 0:
        return '0' * num_zeros + s
    else:
        return s

string_input = input("Enter the string/number: ")
length_input = int(input("Enter total length: "))

print("Result after zfill:", '"' + custom_zfill(string_input, length_input) + '"')