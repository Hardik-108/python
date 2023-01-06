z=int(input("Enter the number "))

def fibonacci_series(n):
    n1=0
    n2=1
    sum=0
    for x in range(n):
        if x==n1:
            print(n1)
        elif x==n2:
            print(n2)
        else:
            sum = n1 + n2
            n1=n2
            n2=sum
            print(sum)

# fibonacci_series(z)


def fibonacci_recursive(x):
    n1=1
    n2=2
    
    if x==n1:
        return 0
        
    elif x==n2:
        return 1

    else:
        return fibonacci_recursive(x-1)+ fibonacci_recursive(x-2)

     
v=fibonacci_recursive(z)
print(v)
