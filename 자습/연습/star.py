n = 5  
t = 1
for i in range(n):#세로
    #가로 
    for i in range(n-1):
        print(" ",end="")
    n-=1
    for j in range(t):
        print("*",end="")
    t+=1
    print()

count =1
num =4
blank = num - 1
#세로
#가로
for _ in range(num):  #공백 먼저
    for _ in range(blank):
        print(" ", end = "")
       
    for _ in range(count):#*
        print("*", end = "")
    print()
    blank -= 1
    count += 2
         