s = [int(input()) for _ in range(10)]
c = []
for i in s:
    a = int(i)  % 42 
    if a not in c:
        c.append(a)
     
print(len(c))
