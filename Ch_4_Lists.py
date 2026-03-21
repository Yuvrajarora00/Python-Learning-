# Lists
# lists are mutable means we can change them after creating them.


a = ["apple","bannana",74,True,74.5,"grapes"]
# print(a[1][3]) 
# in first index we write what we want to access in that index and in second index we write which word or letter we want to access in that index.
print(a[2])
#  if we want to access any index we just write the index number in square brackets.
a[1] = "orange"  # we can change the value of any index by just assigning a new value to that index.
print(a)


# List methods 
a.append("hello") # this will add "hello" at the end of the list.
# print(a)


l1 = [23,345,667,8,96,5,443]
l1.sort()# this will sort the list in ascending order.
l1.reverse() # this will reverse the list. 
l1.insert(4,6736) # this will insert 6736 st the index number 4.
l1.remove(96) # this will remove 96 from the list.
l1.pop(3) # this will print the only index number 3 .
l1.extend([45,78,90]) # this will add 45,78,90 at the end of the list.
l1.clear() # this will clear the entire list.
# l1.index(443) # this will return the index number of 443.
l1.count(5) # this will retrun how many times 5 is present in list.
l1.copy() # this will create a copy of a list.
print(l1)


