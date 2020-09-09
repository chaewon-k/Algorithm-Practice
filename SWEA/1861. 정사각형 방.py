def find(start_x, start_y):
    global count
    for d in range(4):
        temp_x = start_x + dx[d]
        temp_y = start_y + dy[d]
        if 0<= temp_x < N and 0<= temp_y < N:
            if square[start_x][start_y] + 1 == square[temp_x][temp_y]:
                visited[temp_x][temp_y] = 1
                count += 1
                find(temp_x, temp_y)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = int(input())
for t in range(T):
    N = int(input())
    max_cnt = -1
    count = 1
    start = 100000
    square = [list(map(int,input().split())) for _ in range(N)]
    visited = list([0] * N for _ in range(N))
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                visited[x][y] = 1
                find(x, y)
                if max_cnt < count:
                    max_cnt = count
                    start = square[x][y]
                elif max_cnt == count and start > square[x][y]:
                    start = square[x][y]
                count = 1
    print(f'#{t+1} {start} {max_cnt}')
