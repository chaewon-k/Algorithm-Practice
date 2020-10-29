def dfs(x, y, cnt):
    global mini
    if cnt >= mini:  return
    if x == N-1 and y == N-1:
        if cnt < mini:
            mini = cnt
            return

    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if dx<N and dy<N:   dfs(dx,dy,cnt+arr[dx][dy])

dir = [(1,0), (0,1)]
T = int(input())
for t in range(1, T+1):
    mini = 10000000
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dfs(0,0,arr[0][0])
    print(f'#{t} {mini}')