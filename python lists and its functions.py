# LISTS AND ITS FUNCTIONS

grocery=["bhindi","potato","onion","carrot","capsicum"]

# COMMAND TO ADD ITEMS IN THE LIST
grocery.append("beetroot")
print(grocery)

numbers=[1,8,5,23,9]
numbers.sort()
print(numbers)
numbers.insert(1,34)
print(numbers)
numbers.remove(8)
print(numbers)

# LIST IS MUTABLE (MUTABLE- can change)
# TUPLE IS IMMUTABLE (IMMUTABLE-cannot change)

tp=(1, 2, 3)     #this is tuple
print(tp)
# tp[1]=4 (error because tuple is immutable)