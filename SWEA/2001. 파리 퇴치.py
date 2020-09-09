T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    bugs_map = [list(map(int, input().split())) for _ in range(N)]

    maxi = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = 0
            for m in range(M):
                for n in range(M):
                    temp_sum += bugs_map[i+m][j+n]
            if maxi < temp_sum: maxi = temp_sum

    print(f'#{t+1} {maxi}')