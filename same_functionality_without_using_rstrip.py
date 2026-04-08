#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

text = input("Enter a string: ")

end_index = len(text) - 1

while end_index >= 0 and text[end_index] == ' ':
    end_index -= 1

result = text[:end_index + 1]

print("String after removing trailing spaces:", repr(result))