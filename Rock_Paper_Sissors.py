from random import randint

c = ["Rock", "Paper", "Sissors"]

computer = c[randint(0, 2)]

player = True
player_score = 0
computer_score = 0


while player == True:
    player = input(str("Rock, Paper, Scissors? ")).capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose", computer, "cuts", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cuts", computer)
            player_score += 1
    else:
        print("That's not a valid play. Check your spelling!")

    # player = False
    # computer = c[randint(0, 2)]

    play_again = input("Play again? y/n: ")
    if play_again == "y" or "yes":
        player = True
    if play_again == "n":
        player = False
        print(
            f"Player's score is {player_score}, computer's score is {computer_score}.")
        break
