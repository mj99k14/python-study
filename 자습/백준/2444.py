  


# n = int(input("")) 
# q = 3
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
# for a in range(n-1):
#     print(" " * (a + 1 ) + "*" * (n - 1 - a + q)) # 7,5,3,1
#     q-=1


# # 1,3,5 3,1, 3

# #1,3,5,7,5,3,1 4

# #1,3,5,7,9,7,5,3,1 5

n = int(input())


for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

for i in range(n-1):
    print(" " * (i + 1) + "*" * (2 * (n - i - 2) + 1))
