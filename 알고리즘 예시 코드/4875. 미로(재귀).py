def dfs(x,y):
    if maze[x][y] == '2':
        return 1
    visited[x][y] = 1
    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if 0<=dx<N and 0<=dy<N and maze[dx][dy] != '1' and visited[dx][dy] == 0:
            if dfs(dx,dy):
                return 1
    return 0

dir = [(-1,0),(1,0),(0,-1),(0,1)]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0]*(N+1) for _ in range(N+1)]

    flag = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                result = dfs(i, j)
                flag = -1
                break
        if flag == -1:
            break
    print(result)