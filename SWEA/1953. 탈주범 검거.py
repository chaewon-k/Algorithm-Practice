def bfs(r, c):
    global cnt
    queue = []
    queue.append((r,c))
    visited[r][c] = 1
    while queue:
        x, y = queue.pop(0)
        cnt += 1
        if visited[x][y] < L:
            for d in range(4):
                dx, dy = x + dir[d][0], y + dir[d][1]
                if 0<=dx<N and 0<=dy<M and not visited[dx][dy]:
                    if dirs[arr[x][y]][d] and dirs[arr[dx][dy]][(d+2)%4]:
                        queue.append((dx,dy))
                        visited[dx][dy] = visited[x][y] + 1
    return

dirs = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0],
        [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
dir = [(0,1),(1,0),(0,-1),(-1,0)]

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    bfs(R,C)
    print(f'#{t} {cnt}')