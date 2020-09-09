def dfs(row, p):
    global probability, N
    if row == N:
        if probability <= p:
            probability = p
            return
    else:
        if p <= probability:    return
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(row + 1, p * task[row][i] / 100)
                visited[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    task = [list(map(int, input().split())) for _ in range(N)]
    probability = 0
    visited = [0] * N
    dfs(0,1)
    print(f'#{t+1} {format(probability*100,".6f")}')