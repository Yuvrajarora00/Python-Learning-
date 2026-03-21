# # single inheritance


# class Single:
#     def __init__(self, name, age, college):
#         self.name = name
#         self.age = age
#         self.college = college
#         print(f"hello my name is {self.name} and my age is {self.age}")
#         print(f"my college is {self.college}")


# class Hello(Single):
#     def Hi(self, college):
#         self.college = college
#         print(f"I am student in {self.college}")


# print("|----------------------------------------|")
# print("|         student details 1              |")
# print("|----------------------------------------|")

# S = Single("yuvraj", 83, "LLR college\n")

# print("---------------------------------------------------------------------\n")
# print("|----------------------------------------|")
# print("|         student details 2              |")
# print("|----------------------------------------|")

# c1 = Hello("yuj", 67, "dm collge")


# Multi-level Inheritance
class Single:
    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college
        print(self.good())
        print(f"hello my name is {self.name} and my age is {self.age}")
        print(f"my college is {self.college}")

    def good(self):
        return "hello there i am good,"


class Hello:
    def Hi(self):
        print(self.good())


class Yuvi(Hello, Single):
    def good(self):
        return "hello there i am good,"


S = Single("yuvraj", 83, "LLR college\n")
# c1 = Hello()
P1 = Yuvi("yuvraj", 73, "dm clg")
# P1.good()
