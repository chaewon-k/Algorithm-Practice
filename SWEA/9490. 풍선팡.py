dx = [0,0,-1,1]
dy = [-1,1,0,0]

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    balloon_map = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0
    for i in range(N):
        for j in range(M):
            summ = balloon_map[i][j]
            for k in range(4):
                for l in range(balloon_map[i][j]):
                    temp_x = i+dx[k]*(l+1); temp_y = j+dy[k]*(l+1)
                    if 0 <= temp_x < N and 0 <= temp_y < M:
                        summ += balloon_map[temp_x][temp_y]
            if summ > maxi:
                maxi = summ
    print(f'#{t+1} {maxi}')
