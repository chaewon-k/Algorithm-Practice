def dfs(n, temp_prob):
    global result
    if temp_prob <= result:
        return
    if n == N:
        if temp_prob > result:
            result = temp_prob
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, temp_prob*prob[n][i])
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    result = 0
    N = int(input())
    prob = [list(map(lambda x : int(x)/100, input().split())) for _ in range(N)]
    visited = [0]*N
    dfs(0, 1)
    # print(f'#{t} {(result*100):.6f}')
    print('#{} {:6f}'.format(t, result*100))