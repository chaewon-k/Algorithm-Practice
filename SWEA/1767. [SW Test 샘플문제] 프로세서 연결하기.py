def check_path(d, n):
    dx, dy = core_list[n][0] + d[0], core_list[n][1] + d[1]
    while 0 <= dx < N and 0 <= dy < N:
        if arr[dx][dy] == 1:
            return False
        dx += d[0]
        dy += d[1]
    return True


def dfs(n,cnt, stack, core_connected):
    global mini, core_num

    if n == len(core_list):
        if core_num < len(core_connected):
            mini = cnt
            core_num = len(core_connected)
        if core_num == len(core_connected) and cnt < mini:
            mini = cnt
        return 0

    for d in dir:
        temp_cnt = 0
        if check_path(d, n) == False:
            continue
        else:
            core_connected.append(core_list[n])
            dx, dy = core_list[n][0] + d[0], core_list[n][1] + d[1]
            while 0 <= dx < N and 0 <= dy < N:
                temp_cnt += 1
                stack.append((dx,dy))
                arr[dx][dy] = 1
                dx += d[0]
                dy += d[1]

            dfs(n+1, cnt+temp_cnt, [], core_connected)

            for i in stack:
                arr[i[0]][i[1]] = 0
            stack = []
            core_connected.pop(-1)

            dfs(n + 1, cnt, [], core_connected)


dir = [(-1,0),(1,0),(0,-1),(0,1)]
T = int(input())
for t in range(1, T+1):
    mini = 100000000
    core_num = -1
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    core_list = []
    core_connected = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:  core_list.append((i,j))
    stack = []
    dfs(0,0,stack, core_connected)
    print(f'#{t} {mini}')