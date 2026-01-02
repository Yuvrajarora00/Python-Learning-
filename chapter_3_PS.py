# question 1

a = input("enter your name : ")
print(f"Good Afternoon, {a}") # f string is used to print the name entered by user after what we want to print.

# question 2

letter = ''' dear <|NAME|>
You are selected!
<|date|>'''

print(letter.replace("<|NAME|>", "yuvraj").replace("<|date|>", "11 September 2025"))



# question 3 find Double space

b =  "this is a  string"
print(b.find("  ")) # if it gives -1 that means there is no double space. it works on all strings like name or words etc.

# Strings are immutable means we cannot change them once created. we can create a new string but cannot change the existing one.

print(b.replace("  "," "))  # this will replace double space with single space. this will create a new string. not change the existing one.


c = "dear harry,\n\tthis python course is nice.\nthank you!"
print(c)
