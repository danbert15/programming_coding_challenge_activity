#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

def my_center(text, width):
    if width <= len(text):
        return text

    total_spaces = width - len(text)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    return " " * left_spaces + text + " " * right_spaces

string = input("Enter a string: ")
width = int(input("Enter total width: "))

centered = my_center(string, width)
print(f"'{centered}'")