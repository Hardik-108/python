# ROCK , PAPER AND SCISSORS

import random as r
Turn = 5
player = 0
computer = 0
while (True):
    x = input("Enter R for rock , P for paper , S for Scissors\n")
    Turn = Turn-1

    z = ["R", "S", "P"]
    y = r.choice(z)
    print(y)
    if y == x:
        print("Tie")
        print("Turn left=", Turn)
        print("Your Score=", player)
        print("Computer Score=", computer)
    elif y == "R" and x == "P" and Turn != 0:
        player = player+1
        print("You Won")
        print("Turn left=", Turn)
        print("Your Score=", player)
        print("Computer Score=", computer)
    elif y == "S" and x == "R" and Turn != 0:
        player = player+1
        print("You Won")
        print("Turn left=", Turn)
        print("Your Score=", player)
        print("Computer Score=", computer)
    elif y == "P" and x == "S" and Turn != 0:
        player = player+1
        print("You Won")
        print("Turn left=", Turn)
        print("Your Score=", player)
        print("Computer Score=", computer)
    elif y == "P" and x == "R" and Turn != 0:
        computer = computer+1
        print("You Lose")
        print("Turn left=", Turn)
        print("Your Score=", player)
        print("Computer Score=", computer)
    elif y == "R" and x == "S" and Turn != 0:
        computer = computer+1
        print("You Lose")
        print("Turn left=", Turn)
        print("Your Score=", player)
        print("Computer Score=", computer)
    elif y == "S" and x == "R" and Turn != 0:
        computer = computer+1
        print("You Lose")
        print("Turn left=", Turn)
        print("Your Score=", player)
        print("Computer Score=", computer)
    if Turn == 0:
        print("GAME OVER!")
        print("Your Score=", player)
        print("Computer Score=", computer)

        break
