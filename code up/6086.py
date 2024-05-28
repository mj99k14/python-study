n = int(input())
a = int(0)
s = int(0)
while True:
    a += 1
    s += a
    if s >= n:
        break

print(s)