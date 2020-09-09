def dfs(s, num):
    stack = []
    stack.append(s)
    visited[s] = 1
    while stack:
        start = stack.pop(0)
        for j in relation[start]:
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    relation = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)
    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N + 1):
        if visited[i]:	continue
        else:
            dfs(i, N+1)
            cnt += 1
    print(f'#{t+1} {cnt}')