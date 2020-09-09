def dfs(r, c):
    if maze[r][c] == '3':   return 1
    else:
        v[r][c] = 1
        for d in range(4):
            x = r + dx[d]; y = c + dy[d]
            if 0<= x < N and 0<= y <N and maze[x][y] != '1' and v[x][y] == 0:
                if dfs(x, y):    return 1
        return 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int(input())
for t in range(T):
    N = int(input())
    maze = [input() for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    r_start = c_start = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                r_start, c_start = i, j
                break
    result = dfs(r_start, c_start)
    print(f'#{t+1} {result}')