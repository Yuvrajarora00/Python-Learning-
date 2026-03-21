# Intro

# Positive slicing
a = "yuvraj"
b = a[1:3]
c = a[:6]
d = a[2:]

#Negative slicing
e = a[-5:-2]
f = a[-6:]
g = a[:-1]

print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


#slicing 

h = 'abcdefghijklmnop'
i = h[2:8:4]
print(i)


# string FUNCTION

#case conversion
j = "Hello World"
k = j.upper()    #converts to uppercase all letters
l = j.capitalize()  #converts first letter to uppercase
m = j.title()      #converts first letter of each word to uppercase 
n = j.lower()   #converts to lowercase all letters
o = j.swapcase()  #swaps the case of each letter means uppercase to lowercase and lowercase to uppercase
print(k)
print(l)
print(m)
print(n)
print(o)    

#whitespace removal
p = "   Hello World   "
q = p.strip()   #removes whitespace from both sides
r = p.lstrip()  #removes whitespace from left side
s = p.rstrip()  #removes whitespace from right side
print(q)
print(r)
print(s)     

# Searching and replacing

# s.find("pro") → 7
# s.index("pro") → 7 (error if not found)
# s.count("o") → 2
# s.startswith("py") → True
# s.endswith("ing") → True

t = "python programming"
u = t.find("pro") #finds the index of first occurrence of substring "pro"
v = t.index("pro")  #same as find but raises error if substring not found
w = t.count("o")    #counts the occurrences of substring "o"
x = t.startswith("py")  #checks if string starts with substring "py"
y = t.endswith("ing")   #checks if string ends with substring "ing"
print(u)
print(v)
print(w)
print(x)
print(y)

# Replacement
z = t.replace("python", "java")  #replaces substring "python" with "java"
print(z)

# Splitting and Joining
aa = "apple,banana,cherry"
ab = aa.split(",")  #splits the string into a list using "," as delimiter
ac = "-".join(ab)   #joins the list into a string using "-" as separator
print(ab)
print(ac)

# checking string type

# s.isdigit() → True
# s.isalpha() → False
# s.isalnum() → True
# s.isspace() → False
# s.islower() / s.isupper()

ad = "Hello123"
ae = ad.isalpha()   #checks if all characters are alphabetic means letters
af = ad.isdigit()   #checks if all characters are digits means numbers
ag = ad.isalnum()   #checks if all characters are alphanumeric (letters and numbers mixed)
ah = ad.isspace()   #checks if all characters are whitespace means spaces, tabs, newlines
ai = ad.islower()  #checks if all characters are lowercase letters
print(ae)
print(af)
print(ag)   
print(ah)
print(ai)

# length and formatting
aj = "Hello World"
ak = len(aj)   #returns the length of the string spaces included
al = "Formatted string: {}".format(aj)  #formats the string using format method  
am = f"Formatted string using f-string: {aj}"  #formats the string using f-string
print(ak)
print(al)
print(am)

#Removing prefix and suffix
an = "unhappy"
ao = an.removeprefix("un")  #removing from starting "un"
ap = "running"
aq = ap.removesuffix("ing")  #removing from ending "ing"
print(ao)
print(aq)


# alignment and padding
ar = "Hello"
av = ar.center(20, '*')  #centers the string in a field of width 20, padding with '*'
at = ar.ljust(20, '-')   #left justifies the string in a field of width 20, padding with '-'
au = ar.rjust(20, '+')   #right justifies the string in a field of width 20, padding with '+'
print(av)
print(at)
print(au)       

#escape sequences 
aw = "Hello\tWorld"  #tab space between Hello and World
ax = "Hello\nWorld"  #new line between Hello and World
ay = "He said, \"Hello World!\""  #double quotes inside string same as we write in double comma
az = 'It\'s a beautiful day'  #single quote inside string same as we write in single comma
print(aw)
print(ax)
print(ay)
print(az)