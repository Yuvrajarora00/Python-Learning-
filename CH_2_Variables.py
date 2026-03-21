# variables and datatypes chapter 2
 
a = 39 #integer value
 
b = 34.43 #floating point number 
 
c = "yuvraj" #string
 
d = True #boolean value
 
e = None #none type value 
 
print(a*b) 
 
 
 # Rules in python
 
 # contain only alphabets , digit, underscore
 
 # start with only alphabet and underscore
 
 # 1. @amir = 43 not recoganizeable
 
 # not start with numbers 
 
 # no space allowed

# TYPE CASTING
a = 3

b = "3.4"

r = float(b) # with this we can convert string to float or anything we want 

t = type(a)# with this we can check the type of variable

print(t)

print(r) 


# Type Conversion

# This is a form of concatenation because input() 

# function takes input as string by default.

a = int(input("numbers 1 = "))

# b = input("number 2 = ")

c = int(input("number 3 = ")) #with this we can take integer input.

# print("The value of a + b is : ",a + b)

print("the value of a + c is : ",a + c )