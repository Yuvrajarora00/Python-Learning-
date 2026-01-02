# Tuples
# tuples are immutable means we cannot change them after creating them.
u = () # this is empty tuple
v = (1,) # if we want to add only one element then we have to add a comma after that element.
t = (23,45,67,89,"hello",True,45.6)
print(t[2]) # if we want to access any index we just write the index number in square brackets.


# tuple methods 
# tuples have only two methods
t2 = (23,45,67,89,23,45,23)
a = t2.count(23) # this will return how many times 23 is present in tuple.
print(a)

t3 = (12,34,56,78,90)
b = t3.index(56) # this will return the index number of 56. 
print(b)

# Operations in tuples 

t4 = (1,2,3)
repeated = t4 * 3 # this will repeat the tuple 3 times.
print(repeated)

t5 = (4,5,6)
concatenated = t4 + t5 # this will concatenate two tuples.
print(concatenated)

t6 = (10,20,30,40,50)
membership = 30 in t6 # this will return True if 30 is present in tuple otherwise False.
membership2 = 60 not in t6

print(membership2)
print(membership)

t7 = (5,10,15,20,25)
for item in t7: # this will iterate through each element in the tuple means it will print each element one by one.
    print(item)

# slicing in tuples
t8 = (100,200,300,400,500,600,700)
slice1 = t8[2:5] # this will return a new tuple from index 2 to index 4.
print(slice1)
slice2 = t8[:4] # this will return tuple from starting index to index 3.
print(slice2)
slice3 = t8[3:] # this will return a new tuple from index 3 to last index.
print(slice3)
slice4 = t8[:] # this will return the whole tuple.
print(slice4)
slice5 = t8[::2] # this will return like 1, 3, 5 index elemtnt like jumping 1 element each time.
print(slice5)
slice6 = t8[::-1] # this will return the tuple in reverse order.
print(slice6)

# unpacking tuples
t9 = (1,2,3)
a, b, c = t9 # this will unpack the tuple into three variables a, b, and c.
print(a)
print(b)
print(c)


