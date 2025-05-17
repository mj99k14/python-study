n,m,v = map(int,input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(m):
    graph[i].sort()

vistied = [False] * n

def dfs_stack(start):
    stack = [start]
    vistied[stack] = True

    while stack:
        v = stack.pop()
        print(v,end=' ')
        for neighbor in reversed(graph[v]):
            if not vistied[neighbor]:
                stack.append(neighbor)
                vistied[neighbor] = True

dfs_stack(v)
            