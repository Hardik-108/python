 #print the numbers greater than six from list of strings and number

names=["sonu" , "monu", "raju","tonu",6,3,7,4,8,2,13,65,87]
for name in names:
    if str(name).isnumeric() and name>6:
        print(name)

