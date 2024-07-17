a,b =input().split()
a = a[::-1]
b =b[::-1]
if a < b:
    print(int(b))
else:
    print(int(a))