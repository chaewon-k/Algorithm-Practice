def dfs(idx, core_list, temp, length, num_core):
    global mini, maxi_core
    if idx == len(core_list):
        if num_core > maxi_core:
            maxi_core = num_core
            mini = length
        elif num_core == maxi_core:
            if mini > length:
                maxi_core = num_core
                mini = length
        return

    x, y = core_list[idx][0],core_list[idx][1]
    for d in dir:
        stack = []
        dx, dy = x + d[0], y + d[1]
        while 0 <= dx < N and 0 <= dy < N:              # 갈 수 있는 길인지 판단
            if arr[dx][dy] == 0:                # 한 칸 갈 수 있다
                stack.append((dx,dy))
                dx += d[0]
                dy += d[1]
            else:                               # 한 칸 갈 수 없다.
                stack = []
                break

        if len(stack) > 0:                      # 1. 갈 수 있는 길일 때
            i = 0
            while i < len(stack):   # 가거나
                # print(stack)
                temp[stack[i][0]][stack[i][1]] = 2
                i += 1
            dfs(idx + 1, core_list, temp, length + len(stack), num_core+1)
            i = 0
            while i < len(stack):   # 안 가거나
                temp[stack[i][0]][stack[i][1]] = 0
                i += 1
            dfs(idx + 1, core_list, temp, length, num_core)

    dfs(idx + 1, core_list, temp, length, num_core)          # 2. 갈 수 없는 길일 때


dir = [(0,-1), (0,1), (1,0),(-1,0)] #왼 오 하 상

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    core_list = []
    mini = 100000000
    maxi_core = -1
    side_core_num = 0

    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0 or i == N-1 or j == N-1:
                if arr[i][j] == 1:
                    side_core_num += 1
            else:
                if arr[i][j] == 1:
                    core_list.append((i,j))

    temp_arr = arr[:]
    dfs(0, core_list, temp_arr, 0, 0)
    print(f'#{t+1} {mini}')