# x=5
# y=10
# z=sum((x,y))  #this is built in function
# print(z)


def function1(a,b):
    """this function will calculate average of 2 numbers"""
    average=(a+b)/2
    return average   #it is used to store function in variable
    #if return is not used then it will show none 
a=function1(5,8)  
print(a)
print(function1.__doc__) #.__doc__ is used to print docstring