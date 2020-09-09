def Othello(array, start_x, start_y, team):
    for p in range(8):
        dx = d_x[p]; dy = d_y[p]
        i = start_x; j = start_y
        temp = []
        while (True):
            i += dx; j += dy
            if 0>i or i>=len(array) or 0>j or j>=len(array) or array[i][j] == 0:  break   #index 범위를 넘어가는 경우 or 0을 만날 경우

            if array[i][j] == team:     # 내 팀의 말을 만난다면, 그 사이의 말들을 다 내 팀으로 바꾸고 break.
                for m in range(0, len(temp),2):
                    array[temp[m]][temp[m+1]] = team
                break

            elif array[i][j] != team and array[i][j] != 0:  # 내팀의 말이 아니면, 위치를 저장.
                temp.append(i)
                temp.append(j)
    return array

T = int(input())
d_x = [-1, 1, 0, 0, -1, -1, 1, 1]
d_y = [0, 0, -1, 1, -1, 1, -1, 1]

for t in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    init = N//2
    arr[init][init-1] = arr[init-1][init] = 1
    arr[init-1][init-1] = arr[init][init] = 2

    for m in range(M):
        x, y, team = map(int, input().split())
        arr[x-1][y-1] = team
        arr = Othello(arr, x-1, y-1, team)

    cnt1 = cnt2 = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:  cnt1 += 1
            elif arr[x][y] == 2: cnt2 += 1
    print(f'#{t+1} {cnt1} {cnt2}')