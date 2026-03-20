#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

num = 0

while num <= 100:
    if num % 2 != 0:
        print(num)
    num += 1