graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}


visited = [False] * 4

def dfs(v):
    visited[v] = True
    print(v,end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(0)