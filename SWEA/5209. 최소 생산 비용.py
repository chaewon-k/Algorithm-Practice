def sol(row, temp_sum):
    global result
    if temp_sum > result:   return
    if row == N:
        if result > temp_sum:   result = temp_sum
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            sol(row+1, temp_sum+arr[row][j])
            visited[j] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*(N+1)

    result = 100000000
    sol(0,0)
    print(f'#{t} {result}')