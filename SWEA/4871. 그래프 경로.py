def dfs(v):
    visited[v] = 1
    for w in graph[v]:
        if visited[w] == 0: dfs(w)


T = int(input())
for t in range(T):
    E_list = []
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    start, end = map(int, input().split())

    dfs(start)

    if visited[end] == 1:
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')