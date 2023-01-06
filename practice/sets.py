s=set()
x=[5,6,7,8,9]
from_list=set(x)
print(from_list)
print(type(from_list))

s.add(1)
s.add(2)
s1=s.union({1,2,3})
print(s,s1)