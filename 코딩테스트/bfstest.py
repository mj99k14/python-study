from collections import deque


n, m, v = map(int,input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i].sort()

visited = [False] * n

def bfs_queue(start):
    queue = deque([start])
    visited[start] = True
    