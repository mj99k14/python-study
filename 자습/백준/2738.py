a,b = [],[]
n,m =map(int,input().split())
for i in range(n):
    row = list(map(int,input().split()))
    a.append(row)
for s in range(m):
    col = list(map(int,input().split()))
    b.append(col)
for row in range(n):
    for col in range(m):
        print(a[row][col]+ b[row][col],end=" ")
    print()

