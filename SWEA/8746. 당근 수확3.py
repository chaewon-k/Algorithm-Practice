T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    carrot = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000
    for row in range(1,N):
        for col in range(1,M):
            a = b = c = 0
            for i in range(row,N):
                for j in range(M):
                    c += carrot[i][j]
            for i in range(row):
                for j in range(col):
                    a += carrot[i][j]
                for j in range(col,M):
                    b += carrot[i][j]
            temp_result = max(a, b, c)-min(a, b, c)
            if temp_result < result:    result = temp_result

    print(f'#{t+1} {result}')