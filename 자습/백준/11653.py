# n =int(input())
# a = []
# while True:
#     for i in range(2,n):
#         s = n / i 
#         if s and n % i == 0:
#             s 
            


n =int(input())
d = []
p = []
for i in range(2,n):
    if n % i ==0:
        s = n // i
        d.append(s)
        for s in d:
           a = s //i
           p.append(a)

print(p)