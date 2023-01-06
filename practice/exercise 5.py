# HEALTH MANAGEMENT SYSTEM
print("HEALTH MANAGEMENT SYSTEM")

inp=int(input("Enter 1 Log and 2 for retrieve\n"))

def getdate():
    import datetime
    return datetime.datetime.now()

if inp==1:
    Id=int(input("Enter your id\n"))

    if Id==1:
        x=int(input("Press 5 for Execise and Press 6 for Diet\n"))
        if x==5:
            z=input("what did you do?\n")
            with open("harry_Exercise.txt", "a") as f:
                f.write(str([str(getdate())]) + z)
                
        elif x==6:
                z=input("What did you eat?\n")
                with open("harry_diet.txt", "a") as G:
                    G.write(str([str(getdate())]) + z)
                    
                    
        else:
            print("Enter a valid Number")   
               
    if Id==2:
        x=int(input("Press 5 for Execise and Press 6 for Diet\n"))
        if x==5:
            z=input("what did you do?\n")
            with open("rahul_Exercise.txt", "a") as f:
                f.write(str([str(getdate())]) + z)
        elif x==6:
                z=input("What did you eat?\n")
                with open("rahul_diet.txt", "a") as G:
                    G.write(str([str(getdate())]) + z)
        else:
            print("Enter a valid Number")   

    if Id==3:
        x=int(input("Press 5 for Execise and Press 6 for Diet\n"))
        if x==5:
                z=input("what did you do?\n")
                with open("hammad_Exercise.txt", "a") as f:
                    f.write(str([str(getdate())]) + z)
               
        elif x==6:
                z=input("What did you eat?\n")
                with open("hammad_diet.txt", "a") as G:
                    G.write(str([str(getdate())]) + z)
        else:
            print("Enter a valid Number")     
else:
    Id=int(input("Enter your id\n"))

    if Id==1:
        x=int(input("Press 5 for Execise and Press 6 for Diet\n"))
        if x==5:
            with open("harry_Exercise.txt") as f:
                a=f.read()
                print(a)
          
        elif x==6:
            with open("harry_diet.txt" ) as G:
               b=G.read()
               print(b)
        else:
            print("Enter a valid Number")      
   
    if Id==2:
        x=int(input("Press 5 for Execise and Press 6 for Diet\n"))
        if x==5:
            with open("rahul_Exercise.txt") as f:
                a=f.read()
                print(a)
          
        elif x==6:
            with open("rahul_diet.txt") as G:
               b=G.read()
               print(b)
        else:
            print("Enter a valid Number")      
   
    if Id==3:
        x=int(input("Press 5 for Execise and Press 6 for Diet\n"))
        if x==5:
            with open("hammad_Exercise.txt") as f:
                a=f.read()
                print(a)
          
        elif x==6:
            with open("hammad_diet.txt") as G:
               b=G.read()
               print(b)
        else:
            print("Enter a valid Number")      
   