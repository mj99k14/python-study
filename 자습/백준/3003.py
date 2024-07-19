
w = list(map(int, input().split()))
s = [1,1,2,2,2,8] 
for num in range(len(w)):
    a = s[num] - w[num] 
    print(a, end=" ")
