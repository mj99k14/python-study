n = int(input())
x_l = []
y_l = []
for i in range(n):
    x,y = map(int,input().split())
    x_l.append(x)
    y_l.append(y)

a =  max(x_l) - min(x_l)
b = max(y_l) - min(y_l)
if n == 1:
    print("0")
else:
    print(a *b)