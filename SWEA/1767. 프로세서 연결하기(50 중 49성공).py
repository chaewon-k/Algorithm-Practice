def check_path(d, n):       # 전선 연결할 수 있는지 검사
    dx, dy = core_list[n][0] + d[0], core_list[n][1] + d[1]
    while 0 <= dx < N and 0 <= dy < N:
        if arr[dx][dy] == 1:
            return False
        dx += d[0]
        dy += d[1]
    return True


def dfs(n,cnt, stack, core_connected):
    global mini, core_num
    if core_num < len(core_connected):  # 연결한 core 개수가 더 많으면 최종 전선 수로 저장
        mini = cnt
        core_num = len(core_connected)
    if core_num == len(core_connected) and cnt < mini:  # 연결한 core 개수가 같으면 적게 연결한 전선 수를 저장
        mini = cnt

    if n == len(core_list):     ### 1. 모든 core 점검했을 때
        return
    f = 0
    for d in dir:               ### 2. 모든 core 점검 진행
        temp_cnt = 0
        if check_path(d, n) == False:   # 전선을 연결할 수 없을 경우, 연결하지 않고 다른 방향으로 전환.
            f += 1
            continue
        else:
            core_connected.append(core_list[n])     # 전선을 연결할 수 있는 경우 (전선 연결할 때)
            dx, dy = core_list[n][0] + d[0], core_list[n][1] + d[1]
            while 0 <= dx < N and 0 <= dy < N:      # 전선을 표시하기위해 길을 따라 1을 표시
                temp_cnt += 1
                stack.append((dx,dy))
                arr[dx][dy] = 1
                dx += d[0]
                dy += d[1]

            dfs(n+1, cnt+temp_cnt, [], core_connected)  # 위에서 전선을 표시한 다음 core로 넘어감

            for i in stack:         # stack에 저장해놨던 전선 표시 좌표를 지움 (원상복구) (전선 연결 안할 때)
                arr[i[0]][i[1]] = 0
            stack = []
            core_connected.pop(-1)

            dfs(n+1, cnt, [], core_connected)
    if f == 4:
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

    for i in range(1, N-1):         # 가장자리 제외한 내부 core를 저장.
        for j in range(1, N-1):
            if arr[i][j] == 1:  core_list.append((i,j))
    stack = []
    dfs(0,0,stack, core_connected)  # 전선 표시할 칸 저장할 빈 배열
    print(f'#{t} {mini}')