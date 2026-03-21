# single inheritance
class Single:
    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college
        print(f"hello my name is {self.name} and my age is {self.age}")
        print(f"my college is {self.college}")


class Hello(Single):
    def Hi(self, college):
        self.college = college
        print(f"I am student in {self.college}")


S = Single("yuvraj", 83, "LLR college\n")
c1 = Hello("yuj", 67, "dm collge\n")

print("-----------------------------------------------------------------------------|")
print("-----------------------------------------------------------------------------|")


# Multiple Inheritance
class Single:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def good(self):
        return "hello there i am good,"


class Hello:
    def __init__(self, college):
        self.college = college

    def Hi(self):
        print(f"my college is {self.college}")


class Yuvi(Single, Hello):  # ← Multiple Inheritance
    def __init__(self, name, age, college):
        Single.__init__(self, name, age)
        Hello.__init__(self, college)

    def info(self):
        print(self.good())  # from Single
        print(f"hello my name is {self.name} and my age is {self.age}")
        self.Hi()  # from Hello


S = Yuvi("yuvraj", 83, "LLR college\n")
print()
P1 = Yuvi("yuvraj", 73, "dm clg\n")
S.info()
print()
P1.info()

print("-----------------------------------------------------------------------------|")
print("-----------------------------------------------------------------------------|")
# multi-level inheritance


class one:
    @staticmethod
    def hello():
        print("mu name is ujohnq\n")


class two(one):
    @staticmethod
    def me():
        print("my age us 378\n")


class three(two):
    @staticmethod
    def he():
        print("my clg is jeoiw\n")


c = three()
c.hello()
c.he()
c.me()

print("-----------------------------------------------------------------------------|")
print("-----------------------------------------------------------------------------|")
