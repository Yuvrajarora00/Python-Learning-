# create a list of 7 fruits and display them

fruits = []

# f1 = input("enter fruit name :")
# f2 = input("enter fruit name :")
# f3 = input("enter fruit name :")
# f4 = input("enter fruit name :")
# f5 = input("enter fruit name :")
# f6 = input("enter fruit name :")
# f7 = input("enter fruit name :")
# fruits.append(f1)
# fruits.append(f2)
# fruits.append(f3)
# fruits.append(f4)
# fruits.append(f5)
# fruits.append(f6)
# fruits.append(f7)
# print(fruits)


# to store marks of 6 students in a list and display them in sorted manner
marks = []

f1 = int(input("enter marks here :"))
f2 = int(input("enter marks here :"))
f3 = int(input("enter marks here :"))
f4 = int(input("enter marks here :"))
f5 = int(input("enter marks here :"))
f6 = int(input("enter marks here :"))

marks.append(f1)
marks.append(f2)
marks.append(f3)
marks.append(f4)
marks.append(f5)
marks.append(f6)

marks.sort()
print(marks)

# check that tuple type cannot be changed in python

# tuple = (1,2,3,4,5)
# tuple[2]= 10   # this will give error because tuple is immutable.
# print(tuple)


# to sum a list of 5 numbers
numbers = (2,34,56,75,43)
print(sum(numbers))

a = (23,0,8,8,0,7,0,6,4,0,4)
b = a.count(0)
print(b)