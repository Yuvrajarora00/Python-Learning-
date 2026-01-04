# sets in python
# sets are unordered collections of unique elements
# sets are mutable, meaning we can add or remove elements after creating them
# sets are defined using curly braces {} or the set() function

a = {1, 2, 3, 4, 5} # defining a set using curly braces
print(a)

b = set([4, 5, 6, 7, 8]) # defining a set using the set() function
print(b)

c = {} # this creates an empty dictionary, not a set
print(type(c)) # <class 'dict'>

d = set() # this creates an empty set
print(type(d)) # <class 'set'>

# adding elements to a set
a.add(6)
print(a)

# removing elements from a set
a.remove(3) # raises KeyError if element not found
print(a)
a.discard(10) # does not raise error if element not found
print(a)

# methods of set

# this will return the union of sets a and b
print(a.union(b))