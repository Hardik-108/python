# GUESS THE NUMBER

x=20
guesses=5
while(True):
    inp=int(input("Guess the number\n"))
    guesses= guesses-1

    if inp>x and guesses !=0:
        print("Enter a smaller number ")
        print("your guesses left=",guesses)

    elif inp<x and guesses !=0:
        print("Enter a greater number")
        print("your guesses left=",guesses)

    elif guesses==0:
        print("Game Over ")
        break

    else:
        print("Congratulations you have won")
        break       
