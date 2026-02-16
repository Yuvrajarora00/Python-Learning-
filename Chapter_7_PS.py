# # Problem 1
# num = int(input("enter a number: "))
# i = 1
# for i in range(i, 11):
#     print(f"{num} X {i} : {num*i}")
    
    
# # Problem 2

# l = ["harry","Sehaj","Ravi","soham"]
# for name in l:
#     if name.lower().startswith("s"):
#         print(f"greeting you {name}" )


# problem 3
# num = int(input("enter a number: "))
# i = 1
# while (i<11):
#     print(f"{num} X {i} : {num*i}")
#     i += 1
    
    
# problem 4
# h = int(input("enter a number: "))
# for i in range(2,h):
#     if h % 2 == 0:
#         print("number is prime")
#     break
# else:
#     print("number is not prime")


# problem 5
# k = int(input("enter a number: "))
# i = 0
# sum = 0
# for i in range(i,k+1):
#     sum = sum + i
    
# print(sum)

# # problm 5 with while Loop

# k = int(input("enter a number: "))
# i = 1
# sum = 0
# while i<=k:
#     sum+=i
#     i+=1
    
# print(sum)

# problem 6

# num = int(input('enter a number : '))
# product = 1
# for i in range(1,num+1):
#     product = product * i
# print(product)    


# problem 7
# star = int(input("enter a number: "))
# for i in range(1,star+1):
#     print(" " * (star-i),end=" ")
#     print("*" * (2*i-1),end=" ")    
#     print(" ")


# problem 8
# star2 = int(input("enter a number to print star pattern: "))
# for i in range(1,star2+1):
# #     # print(" " * (star2-i),end="")
#     print("*" * i,end="")
#     print(" ")


# problem 9

star3 = int(input("Enter a Number to Print Pattern: "))
for i in range(1,star3+1):
    if i==1 or i==star3:
        print("*"*star3,end="")
    else:
        print("*",end="")
        print(" " * (star3-2),end="")
        print("*",end="")
    print("")