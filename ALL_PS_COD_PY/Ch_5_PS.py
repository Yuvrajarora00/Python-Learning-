#  Question 1 to traslate hindi to english

words = {
    "madad": "help",
    "kitab":"book",
    "maktab":"school",
    "ustad":"teacher"
}

word = input("write word you want to traslate : ")

print(words[word])

# Question 2 

s = set()
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))

print(s)


s = {}
name  = input("enter your name : ")
lang = input("enter your language : ")
s.update({name:lang})

name  = input("enter your name : ")
lang = input("enter your language : ")
s.update({name:lang})

name  = input("enter your name : ")
lang = input("enter your language : ")
s.update({name:lang})

name  = input("enter your name : ")
lang = input("enter your language : ")
s.update({name:lang})

print(s)

