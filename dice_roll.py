import random

min = 1
max = 6

roll_dice = "yes"

while roll_dice == "yes" or "y":
    print("Rolling Dice!")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_dice = input("Roll again? ")
    if roll_dice == "no":
        break
