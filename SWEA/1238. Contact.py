def bfs(s):
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        s = queue.pop(0)
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[s] + 1

for t in range(10):
    N, start = map(int, input().split())
    call_list = list(map(int, input().split()))
    graph = [[] for _ in range(max(call_list)+1)]
    visited = [0]*(max(call_list)+1)

    for i in range(0,N,2):
        graph[call_list[i]].append(call_list[i+1])

    bfs(start)

    maxi = max(visited)
    for i in range(len(visited)-1, 0, -1):
        if visited[i] == maxi:  break
    print(f'#{t+1} {i}')