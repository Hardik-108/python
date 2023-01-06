#PROJECT: ROCK ,PAPER AND SCISSORS GAME
import random as r

# Global variables 
Turn=5
player=0
computer=0

# Reusable function 
def showdata(outcome):
    print(outcome)
    print("Turn left=" ,Turn)
    print("Your Score=",player)
    print("Computer Score=",computer)

# Program starts from here 
if __name__ =="__main__":

    while (True):
        x=input("Enter R for rock , P for paper , S for Scissors\n").upper()
        Turn=Turn-1
        z=["R" , "S" , "P"]
        y=r.choice(z)
        print("Computer chooses: ",y)
        if y==x:        
            showdata("TIE")
        elif (y=="R" and x=="P" ) or ( y=="S" and x=="R") or (y=="P" and x=="S") and Turn!=0: 
            player=player+1
            showdata("You Won")
        
        elif (y=="P" and x=="R") or (y=="R" and x=="S") or (y=="S" and x=="R") and Turn!=0:
            computer=computer+1       
            showdata("You Lose")          
        if Turn==0:
            print("GAME OVER!")
            print("Your Score=",player) 
            print("Computer Score=",computer)
            break  
