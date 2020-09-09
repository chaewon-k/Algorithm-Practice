def bfs(x, y):
    queue = []
    visited[x][y] = 1
    queue.append([x,y])
    while queue:
        x, y = queue.pop(0)
        if maze[x][y] == '3':
            return visited[x][y]-2
        for d in range(4):
            temp_x, temp_y = x + dx[d], y + dy[d]

            if 0<=temp_x<N and 0<=temp_y<N and maze[temp_x][temp_y] != '1' and not visited[temp_x][temp_y]:
                queue.append([temp_x, temp_y])
                visited[temp_x][temp_y] = visited[x][y] +1
    return 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for t in range(T):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0]*(N+1) for _ in range(N+1)]
    for start_x in range(N):
        for start_y in range(N):
            if maze[start_x][start_y] == '2':
                count = bfs(start_x, start_y)

    print(f'#{t+1} {count}')