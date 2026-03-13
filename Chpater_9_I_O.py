# this will read and print the whole file 

f = open("poem.txt","r")
data = f.read()
print(data)
f.close()

# and if u want to read only few characters use this this includes space also as characters

a = open("poem.txt","r")
data1 = a.readline(5)
print(data1)
a.close()

# # if u want to write in the file this method write in your file but this will delete all your old data u write in the file.

b = open("poem2.txt","w")
b.write("heloooo")
b.close()


# this will create a new file and open it for writing

c = open("poem3.txt","x")
c.write("hello world!")
c.close()

# with this we will write our content at the end of the file 

d = open("poem.txt","a")
d.write("hello world i am yuvi")
d.close()


# with this we csan read and write in the file in binary mode

e = open("poem.txt","rb")
data = e.read()
print(data)
e.close()


# USE OF + MODE WITH ALL


# r+  | Read + Write (file must exist) 
# w+  | Write + Read (deletes old data)
# a+  | Append + Read
# rb+ | Read + Write in binary

