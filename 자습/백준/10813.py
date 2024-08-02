n,m = map(int,input().split())
b = [a for a in range(1,n+1)]
for _ in range(m):
    i,j =map(int,input().split())
    b[i-1],b[j-1] = b[j-1],b[i-1]
for s in b:
    print(s,end=" ")
