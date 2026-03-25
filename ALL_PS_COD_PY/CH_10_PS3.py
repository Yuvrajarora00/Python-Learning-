# # super function
# class employee:
#     def yuvi(self):
#         print("my name is yuvi")

#     a = 5


# class programmer(employee):
#     def anju(self):
#         print("my name is anju")

#     b = 4


# class manager(programmer):
#     def kapil(self):
#         super().anju()
#         print("my name is kapil")

#     c = 3


# c = manager()
# c.kapil()
# print(c.c, c.b, c.a)


# Class method


# class yuvraj:
#     a = 91
#     @classmethod  # this method will not change the value of a in the last
#     def mine(self):
#         print(f"the value of a is {self.a}")


# f = yuvraj()
# f.a = 2
# f.mine()


# class Student:
#     school = "LLR College"
#     count = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.count += 1

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

#     @classmethod
#     def total_students(cls):
#         print(f"Total students: {cls.count}")

#     def info(self):
#         print(f"{self.name} | Age: {self.age} | School: {Student.school}")


# s1 = Student("Yuvraj", 20)
# s2 = Student("Anju", 22)
# s3 = Student("Kapil", 21)

# s1.info()
# s2.info()
# s3.info()
# Student.change_school("DM College")

# s1.info()
# s2.info()
# s3.info()

# Student.total_students()
