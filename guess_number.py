import random

play = True
count = 0

while play == True:
    number = random.randint(1, 100)
    guess = int(input("Enter your guess: "))

    while number != guess:
        count += 1
        if guess < number:
            print("Guess higher")
            guess = int(input("Enter your guess: "))
        elif guess > number:
            print("Guess lower")
            guess = int(input("Enter your guess: "))
        if guess == number:
            print(
                f"You got it, the number was {number} and you got in in {count} tries.")

    play_again = input("Play again? y/n: ")
    if play_again == "y":
        play = True
    elif play_again == "n":
        play = False
        print("Thanks for playing")
        break
