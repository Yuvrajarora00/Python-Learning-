# sets in python
# sets are unordered collections of unique elements
# sets are mutable, meaning we can add or remove elements after creating them
# sets are defined using curly braces {} or the set() function
# sets don't repeat elements

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

# this will return the intersection of sets a and b
print(a.intersection(b))

# this will return the difference of sets a and b (elements in a but not in b)
print(a.difference(b))

# Operators on sets

# union
c = {1, 2, 3}
d = {3, 4, 5}
print(c | d)   # merge  

# intersection
print(c & d)   # common elements

# difference
print(c - d)   # elements in c but not in d

# symmetric difference
print(c ^ d)   # elements in either c or d but not in both

# checking membership
print(2 in c)  # True

print(5 not in c)  # True


# set comprehension
squared_set = {x**2 for x in range(10)}
print(squared_set)

# sorted 2 sets after merge
unsorted_set1 = {842309, 3, 9, 1}
unsorted_set2 = {8, 2, 7, 834032, 7823}
merged_set = unsorted_set1.union(unsorted_set2)
sorted_set = sorted(merged_set)
print(sorted_set)