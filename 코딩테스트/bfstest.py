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

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] =  True
bfs_queue(v)

