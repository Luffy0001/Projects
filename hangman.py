import random

play = True

while play == True:
    name = input("What is your name? ").capitalize()

    print(f"Welcome to my hangman game, {name}")

    with open("word_list.TXT", "r") as f:
        words = f.readlines()

    word = random.choice(words)[:-1]
    guesses = " "
    turns = 10

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("*", end=" ")
                failed += 1

        if failed == 0:
            print(f"\nYou won, {name}!")
            break

        guess = input("\nEnter a letter: ")
        guesses += guess

        if guess not in words:
            turns -= 1
            print("Wrong guess")
            print(f"You have {turns} left\n")

        if turns == 0:
            print(f"You lose! the word was, \"{word}\"")

    play_again = input("Play again? y/n: ")
    if play_again == "y":
        play = True
    elif play_again == "n":
        play = False
        print("Thanks for playing")
        break
