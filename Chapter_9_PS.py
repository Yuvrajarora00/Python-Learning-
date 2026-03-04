# # problem 1

# # f = open("poem2.txt","r")
# # c = f.read()
# # if ("heektkl" in c):
# #     print("yes there is word twinkle")
# # else:
# #     print("no there is no word like this")
# # f.close


# # # problem 2
# # import random

# # def game():
# #     print("you are playing a game")
# #     score = random.randint(1,100)
    
# #     # fetch the hiscore
# #     with open("hiscore.txt") as f: 
# #         hiscore = f.read()
# #         if (hiscore != ""):
# #             hiscore = int(hiscore)
# #         else:
# #             hiscore = 0
            
# #     print(f"your score: {score}")
# #     if score>hiscore:
# #         with open("hiscore.txt","w") as f:
# #             f.write(str(score))
            
# #         return score
    
    
# # game()

# # problem 3

# # def table(n):
# #     table = ""
# #     for i in range(1,11):
# #         table += f"{n} X {i} = {n*i}\n"
        
# #     with open(f"tables/table_{n}.txt","w") as f:
# #         f.write(table)

 
# # for i in range(2,21):
# #     table(i)
    
    
# # problem 4

# word = "donkey"

# with open("donkey.txt","r") as f:
#     content = f.read() 
    
# newcontent = content.replace(word,"#####")

# with open("donkey.txt","w") as f:    
#     f.write(newcontent)
    
    
    
# # problem 5
# word = "donkey"

# with open("donkey.txt","r") as f:
#     content = f.read() 
    
# newcontent = content.replace(word,"@"*len(word))

# with open("donkey.txt","w") as f:    
#     f.write(newcontent)
    
    
    
# # problem 6
# with open("python.txt","r") as f:
#     content = f.read()
#     if ("python" in content):
#         print("there is word python")
#     else:
#         print("there is no word like that")


# problem 6


with open("pyec.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"python word is present in line number: {lineno}")
        break
    lineno += 1
else:
    print("there is no word like that")