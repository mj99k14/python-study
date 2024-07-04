t = int(input())
s = [ ]
for i in range(t):
    a,b = input().split()
    a  = int(a)
    for ia in b:
        s.append(ia * a)
    print(' '.join(s))
print()

a = int(input())
for i in range(a):
  b, c = input().split()
  for i in range(len(c)):
    print(int(b) * c[i], end='')
  print()                                       