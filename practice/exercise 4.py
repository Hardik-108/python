# PATTERN PRINTING


x=int(input("enter a number\n"))

n=int(input("enter 0 for false or 1 for true\n"))

if n==0:
    for z in range(x):
        for c in range(z+1):
            print("*", end="")
        print("\n")
else:
    for z in range(x,0,-1):
    
        for v in range(z):
            print("*" , end="")
        print("\n")
