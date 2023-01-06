names=["sonu" , "monu", "raju","tonu",6,3,7,4,8,2,13,65,87]
names_length =len(names)
print(names_length)
x=0
while x<13:
    
    if str(names[x]).isnumeric() and names[x]>6:
        print(names[x])
    x=x+1