import random

num = random.randint(1, 100)

Guess = None

while Guess != num:
    try:
        Guess = int(input("Enter a number: "))
        if Guess > num:
            print("To high")
        elif Guess < num:
            print("To low")
        else:
            print("You got it")
            break
    except ValueError:
        print("Enter a number only! Try again")
