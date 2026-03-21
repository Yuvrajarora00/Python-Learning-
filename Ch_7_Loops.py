# for loop syntax
for i in range(1 ,60):
    print(i)


# while loop Syntax

i = 1
while(i<6):
    print(i)
    i+=1

# print list with while loop

list = [2,"yuvraj", True, 23.23, "hello world"]
i = 1

while(i<len(list)):
    print(list[i])
    i+=1


# using for loops in tuples and also in sorted method

tuple = (23,32,4,354,43,213)

for i in sorted(tuple,reverse=True):
    print(i)


# using of break and continue

for i in range(100):
    if(i == 35):
        break # this function can exit the loop on 35
    print(i)


for i in range(100):
    if (i == 32):
        continue # this function skip the number and jump on the next one.
    print(i)