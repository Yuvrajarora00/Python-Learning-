# # problem 1
# class Programmer:
#     @staticmethod
#     def __micro__():
#         print("microsoft employee")

#     def __init__(self, name, language):
#         Programmer.__micro__()
#         self.name = name
#         self.language = language
#         print(f"name is : {self.name} and language is: {self.language}")


# P1 = Programmer("yuvraj", "python")
# print("----------------------------------------")
# P2 = Programmer("rahul", "Javascript")
# print("----------------------------------------")
# P3 = Programmer("mayank", "Swift")
# print("----------------------------------------")
# P4 = Programmer("shilpa", "Python")
# print("----------------------------------------")


# Problem 2


# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         return self.n * self.n

#     def cube(self):
#         return self.n * self.n * self.n

#     def square_root(self):
#         return self.n**1 / 2


# C1 = Calculator(4)
# print(C1.square(), "\n", C1.cube(), "\n", C1.square_root())


# problem 3

# from random import randint


# class Railway:
#     def __init__(self, trainno):
#         self.trainno = trainno

#     def book(self, fro, to):
#         print(f"the ticket is booked in train no {self.trainno} whih is going to {fro} to {to}")

#     def getstatus(self):
#         print(f"your train no is {self.trainno}")

#     def getfare(self, fro, to):
#         print(f"your train ticket fair is {randint(234, 7281)}")


# R1 = Railway(2892)
# R1.book("zira", "delhi")
# R1.getstatus()
# R1.getfare("zira", "delhi")
