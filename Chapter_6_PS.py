# question 1to find greatest of 4 numbers 

a1 = int(input("enter number 1 :"))
a2 = int(input("enter number 2 :"))
a3 = int(input("enter number 3 :"))
a4 = int(input("enter number 4 :"))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print("a1 is greater",a1)
elif(a2 >= a1 and a2 >= a3 and a2 >= a4):  
    print("a2 is greater",a2)
elif(a3 >= a1 and a3 >= a2 and a3 >= a4):
    print("a3 is greater",a3)
elif(a4 >= a1 and a4 >= a2 and a4 >= a3):
    print("a4 is greater",a4)   



#  qestion 2 cheack student pass or fail

marks1 = int(input("enter marks of subject 1 : "))
marks2 = int(input("enter marks of subject 2 : "))
marks3 = int(input("enter marks of subject 3 : "))

total_marks = (100)*(marks1+marks2+marks3)/300

if(total_marks >= 33 and marks1 >=33 and marks2 >=33 and marks3 >= 33):
    print("student is pass",total_marks)
else:
    print("student is fail",total_marks)
    


# question 3 to cheack spam comment or not

a = "join my telegram to win lottery"
a1 = "click this link save money"
a2 = "buy now"

comment = input("enter your comment : ")

if((a in comment) or (a1 in comment) or (a2 in comment)): # in is keyword that returns true and false
    print("this is spam comment")
else:
    print("this is not spam comment")


# Question 4 to

a = input("write a name: ")
if(len(a) < 10):
    print("name is less than 10 characters")
else:
    print("name is greater than 10 characters")



# question 5 to find that name is present in list or not 
a = ["yuvraj", "rohit", "raghav", "divanshu"]
name = input("enter a name : ")

if(name in a):
    print("this name is preset in list")
else:
    print("this name is not present in list")



# question 6 

marks1 = int(input("enter marks : "))

if (marks1 < 100 and marks1 > 90):
    grade = "ex"
if (marks1 < 90 and marks1 > 80):
    grade = "a"
if (marks1 < 80 and marks1 > 70):
    grade = "b"
if (marks1 < 70 and marks1 > 60):
    grade = "c"
if (marks1 < 60 and marks1 > 50):
    grade = "d"
if (marks1 < 50):
    grade = "f"
print("your grade is :", grade)




# Question 7

a1 = input(" enter a name : ")

if("harry" in a1.lower()):  # if we add these strings then if the words are upper case or lower case it will detect 
    print("this post is talking about harry")
else:
    print("this post is not talking about harry")

