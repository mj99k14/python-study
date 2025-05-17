graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}
visited = [False] * 4

def dfs_stack(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v,end=' ')
            for neighbor in reversed(graph[v]):
                stack.append(neighbor)
dfs_stack(0)