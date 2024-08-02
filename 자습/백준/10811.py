n,m = map(int,input().split())
b = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    b[i-1 :j]= b[i-1 :j][::-1] # 그부분만 역순으로 지정해주기 위해서 [::-1] -> 뒤에다 하나더해줌
    
for a in b:
    print(a,end=" ")