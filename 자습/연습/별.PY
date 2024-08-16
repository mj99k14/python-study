# #별 5*5
# n=5
# for i in range(n):#세로
#     for i in range(n):#가로
#         print("*",end="")
#     print()

#   * 
#  ***
# *****
n = 5
s =3
g = 2
for _ in range(s):
    for _ in range(g):
        print("*",end="")
        g -=1
    for _ in range(n):
        print("*",end="")
print()