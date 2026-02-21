# # problem 1 to find the greates number 

# def greatest(a ,b ,c):
#     if a > b and a > c:
#         return a
#     elif b > c and b > a:
#         return b
#     else:
#         return c
        

# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# c = int(input("enter a number: "))
# print(greatest(a,b,c))


# # problem 2 celcius to fehranite

# def new_func(k):
#     return 5 * (k-32)/9

# k = float(input("enter a number to f: "))
# c = new_func(k)
# print(f"{round(c, 2)} degree celcius")


# problem 3

# def print_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return print_sum(n-1) + n
    
# print(print_sum(5))


# problem 4
# def line(k):
#     if(k == 0):
#         return 0
#     print("*" * k)
#     line(k-1)
#     print()
        
# line(3)

# problem 5
# def inc_cm(inc):
#     return inc * 2.54
    
# k = int(input("enter a number to covert inc to cm: "))
# print(inc_cm(k))

# problem 6
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n * i}")

m = int(input("enter a number to print table: "))        
table(m)