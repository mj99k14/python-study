graph = [
    [1, 2],
    [0, 3],
    [0],
    [1]
]

visited = [False] * len(graph)


n,m,v =map(int,input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

visited = [False] * n
