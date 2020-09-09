def dfs(x, y):
    if maze[x][y] == '3':
        return 1
    else:
        visited[x][y] = 1
        for d in range(4):
            temp_x, temp_y = x + dx[d], y + dy[d]
            if 1<= temp_x < N-1 and 1<= temp_y < N-1 and maze[temp_x][temp_y] != '1' and visited[temp_x][temp_y] == 0:
                if dfs(temp_x, temp_y): return 1
        return 0

N = 16
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for _ in range(10):
    T = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    start_x = start_y = 1
    result = dfs(start_x, start_y)
    print(f'#{T} {result}')