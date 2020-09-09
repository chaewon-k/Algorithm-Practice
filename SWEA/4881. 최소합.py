def dfs(row, summ):
    global N, min_sum
    if row == N:
        if min_sum > summ:
            min_sum = summ
            return
    else:
        if summ >= min_sum: return
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                dfs(row + 1, summ + array[row][i])
                v[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    min_sum = 100000000
    dfs(0, 0)
    print(f'#{t+1} {min_sum}')
