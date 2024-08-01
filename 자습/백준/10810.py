n,m = map(int,input().split())
n1 = [0 for _ in range(n)]
for _ in range(m):
    i,j,k=map(int,input().split())
    for a in range(i,j+1):
        n1[a-1] = k

for i in n1:
    print(i,end=" ")
