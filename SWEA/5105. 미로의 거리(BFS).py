def BFS(x, y):
    Q = [(x, y)]
    V[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        if arr[x][y] == '3':
            return V[x][y] - 2
        for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx, dy = x+a, y+b
            if 0 <= dx < N and 0 <= dy < N and not V[dx][dy] and arr[dx][dy] != '1':
                Q.append((dx, dy))
                V[dx][dy] = V[x][y] + 1
    return 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    V = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                print(f'#{t} {BFS(i, j)}')
                break