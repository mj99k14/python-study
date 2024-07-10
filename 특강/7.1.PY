# import os

# result = os.getcwd()

# print(f"{result}:{type(result)}")

# os.chdir("../")

# result = os.getcwd()

# print(f"{result}:{type(result)}")

# result = os.listdir()

# print(f"{result} :{type(result)}")  




import os

# Relative reference
#f_handler = open(r"imgs/test.txt", "r")

# Absolute reference
f_handler = open(r"c:/myGame/imgs/test.txt", "r")

msg = f_handler.read()

print(msg)

f_handler.close()