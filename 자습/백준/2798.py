m, n = map(int,input().split())
s = list(map(int,input().split()))
sum = 0
for i in range(m):
    for s1 in range(i+1, m):
        for a in range(s1+1, m):
            if s[i] + s[s1] +s[a] > n:
                continue
            else:
                sum = max(sum, s[i] + s[s1] + s[a])
print(sum)