from collections import deque
graph = [
    [1, 2],
    [0, 3],
    [0],
    [1]
]

visited = [False] * len(graph)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')

        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] =  True