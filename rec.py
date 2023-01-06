def factorial_interative(n):
    fac=1
    for x in range(n):
        fac=fac* (x+1)
    return fac

z=int(input("Enter the number ")) 

print("Using interative method " , factorial_interative(z))

def factorial_recursive(n):

    if n==1:
        return 1
    else:
        return n* factorial_recursive(n-1)
print("Using recursive method" ,factorial_recursive(z))            