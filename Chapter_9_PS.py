# problem 1

# f = open("poem2.txt","r")
# c = f.read()
# if ("heektkl" in c):
#     print("yes there is word twinkle")
# else:
#     print("no there is no word like this")
# f.close


# # problem 2
# import random

# def game():
#     print("you are playing a game")
#     score = random.randint(1,100)
    
#     # fetch the hiscore
#     with open("hiscore.txt") as f: 
#         hiscore = f.read()
#         if (hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
            
#     print(f"your score: {score}")
#     if score>hiscore:
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
            
#         return score
    
    
# game()


def table(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
        
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range(2,21):
    table(i)