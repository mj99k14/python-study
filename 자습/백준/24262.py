A, B = map(int,input().split())
C= int(input())
D= int(input())

if A * D + B <= C * D and A <= C:
    print(1)
else:
    print(0)