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