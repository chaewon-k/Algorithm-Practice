def match(arr):
    global cnt
    for k in range(len(arr)-1):
        if arr[k] == 1 and arr[k+1] == 2:   cnt += 1

T = 10
for t in range(T):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        col = []
        for j in range(N):
            if magnetic[j][i] != 0: col.append(magnetic[j][i])
        match(col)
    print(f'#{t+1} {cnt}')
