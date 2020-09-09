T = int(input())
for t in range(T):
    N, M, K, H = map(int,input().split())
    land = [list(map(int, input().split())) for _ in range(N)]  
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            site = []
            for m in range(i-1, i+2):
                for n in range(j-1,j+2):
                    if m == i and n == j:   continue
                    else:   site.append(land[m][n])
            maxi = max(site); mini = min(site)
            if 0 <= maxi-mini <= K and 0 <= land[i][j] - mini <= H:   cnt += 1
    print(f'#{t+1} {cnt}')