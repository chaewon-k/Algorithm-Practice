def bfs(v):
    Q = []
    Q.append(v)
    while Q:
        v = Q.pop(0)
        for w in graph[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())
    bfs(start)

    if visited[end] != 0:   print(f'#{t+1} {visited[end]}')
    else:   print(f'#{t+1} 0')