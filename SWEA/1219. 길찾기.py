def dfs(v):
    visited[v] = 1
    print(visited)
    for w in graph[v]:
        if visited[w] == 0: dfs(w)

for _ in range(1):
    T, E = map(int,input().split())
    E_list = list(map(int,input().split()))
    graph = [[] for _ in range(100)]
    visited = [0] * 100

    for i in range(E):
        a, b = E_list[2*i], E_list[2*i+1]
        graph[a].append(b)
    dfs(0)
    if visited[99] == 1:
        print(f'#{T} 1')
    else:   print(f'#{T} 0')