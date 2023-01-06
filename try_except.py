x=input("Enter your first number\n")
y=input("Enter your second number\n")
try:
    print(int(x)+int(y))
except Exception as z:
    print(z)
#the program continues to run after getting error by using try except
print("hello")
