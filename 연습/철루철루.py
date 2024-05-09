# n =5
# for i in range(n):
#     for i in range(n):
#         print("*",end="")
#     print()
#      #세로
#      #가로 
     
     
# for  i in range(5):#세로가 5줄
#     for j in range(i+1):#가로가 세로 보다 +1
#         print("*",end ="")
#     print()
    

# n = 5
# for i in range(n):#세로
#     for i in range(n):#가로
#         print("*",end="")
#     print()
#     n -=1
    #
    # 
#     # 
# n = 5  
# t = 1
# for i in range(n):#세로
#     #가로 
#     for i in range(n-1):
#         print(" ",end="")
#     n-=1
#     for j in range(t):
#         print("*",end="")
#     t+=1
#     print()
# #  *                                                         
#    ***
#   *****
#  *******
# *********  
row_count = 5    #f2누르면 이름 바꿀수있음
star_count = 1
#세로 
#가로
for _ in range(row_count):
    # print for blanks
    for _ in range(row_count - 1):
        print(" ", end = "")

    # print for "*"
    for _ in range(star_count):
        print("*", end = "")

    # print "\n"
    print()  
    
    # update for counts
    row_count -= 1
    star_count += 2

    
    
    
    
    
    