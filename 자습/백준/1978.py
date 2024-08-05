N =int(input())
# for _ in range(N):
s = list(map(int,input().split()))
print(s)
a = []
# for i in s:
#     if s[i] % 1== 0 and s[i] % s[i] == 0:
#         a.append(s)
# aa= sum(a)
# print(len(aa))

for i in range(1,s+1):
    if s[i] % i == 0:
        a.append(s[i])

print(a)
