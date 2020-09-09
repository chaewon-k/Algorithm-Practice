T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    flag = -1
    maxi = 0
    for i in range(N):
        temp_cnt = 0
        flag = -1
        for j in range(M):
            if land[i][j] == 1:
                flag = 1
                temp_cnt += 1
                if j == M-1:
                    if maxi < temp_cnt:
                        maxi = temp_cnt
            else:
                if flag == 1:
                    if maxi < temp_cnt: maxi = temp_cnt
                    temp_cnt = 0
                    flag = -1

    for i in range(M):
        temp_cnt = 0
        flag = -1
        for j in range(N):
            if land[j][i] == 1:
                flag = 1
                temp_cnt += 1
                if j == N-1:
                    if maxi < temp_cnt:
                        maxi = temp_cnt
            else:
                if flag == 1:
                    if maxi < temp_cnt: maxi = temp_cnt
                    temp_cnt = 0
                    flag = -1
                    
    print(f'#{t+1} {maxi}')