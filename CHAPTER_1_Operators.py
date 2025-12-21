# Display_All_Folders.py
import os

path = "new folder"

# List all files and folders
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)
# ...existing code...



#jarvis.py

import pyttsx3

engine = pyttsx3.init(driverName="espeak")

# ✅ FIRST get the voices list
voices = engine.getProperty("voices")

# ✅ THEN use it
engine.setProperty("voice", voices[3].id)  # change index if needed
engine.setProperty("rate", 200)
engine.setProperty("volume", 2.0)

engine.say("Hello Yuvraj, what can I help you with today")
engine.runAndWait()


#Multiline printint in python

print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
 like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
 When the blazing sun is set, and the grass with dew is wet. Then you show your little
 light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
 are.
 Then the traveler in the dark thanks you for your tiny spark. How could he see where to
 go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
 As your bright and tiny spark lights the traveler in the dark, though I know not what you
 are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')

# Operators in python

a  = 1
if (a < 1):
    print("yes")
else:
    print("no")

# +	Addition	10 + 5	15
# -	Subtraction	10 - 5	5
# *	Multiplication	10 * 5	50
# /	Division	10 / 4	2.5
# // Floor division	10 // 4	2
# %	Modulus (remainder)	10 % 4	2
# **	Power	2 ** 3	8

a = 10
b = 3
print(a + b)
print(a // b)
print(a ** b)
print(a % b)
print(a / b)
print(a - b)
print(a * b)

# Comparison Operators in Python

# ==	Equal to	a == b
# !=	Not equal to	a != b
# >	Greater than	a > b
# <	Less than	a < b
# >=	Greater than or equal to	a >= b
# <=	Less than or equal to	a <= b
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical Operators in Python
# and 	Returns True if both statements are true	a < 5 and b < 5
# or	Returns True if one of the statements is true	a < 5 or b < 5
# not	Reverse the result, returns False if the result is true	not(a < 5 and b < 5)
a = 10
b = 20
print(a < 5 and b < 5)
print(a < 5 or b < 5)
print(not(a < 5 and b < 5))

# Assignment Operators in Python
# =	    Assigns a value to a variable	    a = 5
# +=		Adds and assigns a value to a variable	a += 5
# -=		Subtracts and assigns a value to a variable	a -= 5
# *=		Multiplies and assigns a value to a variable	a *= 5
# /=		Divides and assigns a value to a variable	a /= 5
# %=		Modulus and assigns a value to a variable	a %= 5
a = 10
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
a /= 5
print(a)
a %= 5
print(a)        

