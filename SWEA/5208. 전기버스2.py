def dfs(idx, cnt):
    global result
    if result < cnt:
        return
    if idx >= N:
        result = cnt
        return
    for i in range(arr[idx],0,-1):
        dfs(idx+i, cnt+1)

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = result = arr[0]
    dfs(1,0)
    print(f'#{t} {result-1}')