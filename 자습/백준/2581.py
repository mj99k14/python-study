m =int(input())
n = int(input())
a = []
for i in range(m , n+1):
    count = 0
    if i > 1 :
        for s in range(2,i):
            if  i % s == 0:
                count +=1
        if count == 0:
            a.append(i)
if len(a) > 0:
    print(sum(a))
    print(min(a))
else:
    print(-1)



