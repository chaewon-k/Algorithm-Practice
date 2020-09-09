def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in graph[v]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)

def bfs(v):
    stack = []
    stack.append(v)
    while stack:
        temp = stack.pop(0)
        visited2[temp] = 1
        print(temp, end=' ')
        for w in graph[temp]:
            if visited2[w] == 0:
                stack.append(w)
                visited2[w] = 1

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

result2 = []
visited = [0]*(N+1)
dfs(V)
print()
visited2 = [0]*(N+1)
bfs(V)