import random

print('''
Password Generator
==================
''')
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"£$%^&*()_-+=;:@'~#][}{?/>.,<\|1234567890"

number = input("How many passwords do you want? ")
number = int(number)

length = input("How long do you want it to be? ")
length = int(length)

if number > 1:
    print("\nHere are your passwords:")
else:
    print("\nHere id your password:")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)
