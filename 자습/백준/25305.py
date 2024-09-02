# n = int(input())
# a = [ int(input()) for s in range(n)]
# a.sort()
# for i in a:
#     print(i)



n = int(input())
print(*sorted(int(input()) for _ in range(n)), sep='\n')
