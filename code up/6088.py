a,d,n =map(int,input().split())
# c = 0 
# for _ in range(0, n - 1):
#     c += 1
#     a = 1 + d * c
# print(a)

a = int(a)
d = int(d)
n = int(n)

s = a
for i in range(0, n - 1):
    s += d
print(s)





