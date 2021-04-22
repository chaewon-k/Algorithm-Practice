def conflict():
    global remain
    for i in range(N):
        for j in range(N):
            if len(smell_arr[i][j]) > 1:
                sorted(smell_arr[i][j], key= lambda x: x[0])
                temp = smell_arr[i][j].popleft()
                idx_site[temp[0]] = (0,0)
                remain -= 1

def minus_smell():
    global N
    for i in range(N):
        for j in range(N):
            if smell_arr[i][j]:
                smell_arr[i][j][1] -= 1
            if smell_arr[i][j][1] == 0:
                smell_arr[i][j].popleft()

def move_sharks():
    global N, M, K
    # 상어들 이동
    for idx in range(1,M+1):
        x, y = idx_site[idx]
        # 냄새 남기기
        smell_arr[x][y].append((idx, K))
        arr[x][y] = idx

        # 이동 방향 탐색
        smell_idx = (idx-1)*4
        now_dir = shark_now_dir[idx-1]
        flag = False
        prior_row = 0
        # 현재 위치에 해당하는 우선순위 행 찾기
        for i in range(smell_idx, smell_idx+4):
            if shark_prior[i][0] == now_dir:
                prior_row = i
                break
        # 해당 우선순위 쭉 훑어보기
        for j in range(4):
            next_dir = shark_prior[prior_row][j]
            dx, dy = x+dir[next_dir][0], y+dir[next_dir][1]
            # 이동 불가능한 경우
            if arr[dx][dy] != idx and arr[dx][dy] != 0:
                continue
            # 이동 가능한 경우
            else:
                idx_site[idx] = (dx, dy)
                flag = True
                break

        # 아무 길을 못찾았다면 자신의 냄새가 있는 자리로 간다.
        if flag == False:
            for j in range(4):
                next_dir = shark_prior[prior_row][j]
                dx, dy = x + dir[next_dir][0], y + dir[next_dir][1]
                if arr[dx][dy] == idx:
                    idx_site[idx] = (dx, dy)
                    break

    # 냄새 1씩 빼기 & 0이면 지우기
    minus_smell()

    # 충돌시 한 상어만 살아남기
    conflict()




from collections import deque

dir = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
shark_now_dir = list(map(int, input().split()))
shark_prior = [list(map(int, input().split())) for _ in range(M*4)]

smell_arr = [[deque() for _ in range(N)] for _ in range(N)]
idx_site = [() for _ in range(M+1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            idx_site[arr[i][j]] = (i,j)
            # smell_arr[i][j].append((arr[i][j], 4))
remain = M
cnt = 0
while True:
    #종료 조건
    if remain == 1:
        break
    # 상어 이동
    move_sharks()
    cnt += 1

print(cnt)