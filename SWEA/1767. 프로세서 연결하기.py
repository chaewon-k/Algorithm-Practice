

def DFS(idx, core, arr, count, core_cnt):
    global maxi, c_cnt
    x, y = core[idx][0], core[idx][1]
    temp_x, temp_y = x, y

    if idx == len(core):
        if count > maxi:
            maxi = count
            return

    for d in dir:
        dx, dy = d[0], d[1]
        temp_cnt = 0
        while True:
            temp_x += dx
            temp_y += dy
            if temp_x == -1 or temp_x == N or temp_y == -1 or temp_y == N:    # 1. 테두리에 닿았을 경우 (전원공급 가능)
                DFS(idx+1, core, arr, count + temp_cnt, core_cnt)

            elif arr[temp_x][temp_y] == 1 or arr[temp_x][temp_y] == 2:      # 2. 전선이나 core에 겹쳤을 경우
                temp_cnt = 0
                dx *= -1
                dy *= -1
                while True:
                    temp_x += dx
                    temp_y += dy
                    if arr[temp_x][temp_y] == 1:
                        break
                    arr[temp_x][temp_y] = 0
                break

            else:                               # 3. 진행하는 경우
                temp_cnt += 1
                arr[temp_x][temp_y] = 2


dir = [[-1,0],[1,0],[0,-1],[0,1]]
T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    core = []
    maxi = c_cnt = 0    # 최대 전선 개수와 최대 core 개수
    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
        for j in range(1,N-1):
            if i != 0 and i!= N-1 and temp[j] == 1:
                core.append([i,j])  #테두리에 위치한 core는 제외한 나머지 core 좌표들 저장.

    DFS(0,core,arr,len(core), 1)
    print(maxi, c_cnt)