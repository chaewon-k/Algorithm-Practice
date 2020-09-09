def word(arr, n, k, x):
    cnt1 = cnt2 = 0
    num = []
    for j in range(n):
        if arr[x][j] == 1:  cnt1 += 1
        if arr[j][x] == 1:  cnt2 += 1

        if j == n-1:
            num.append(cnt1)
            num.append(cnt2)
            break
        else:
            if cnt1 >= 1 and arr[x][j] == 0:
                num.append(cnt1)
                cnt1 = 0
            if cnt2 >= 1 and arr[j][x] == 0:
                num.append(cnt2)
                cnt2 = 0
    return num

T = int(input())
for t in range(T):
    result = 0
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        num_list = word(arr, N, K, i)
        for m in num_list:
            if m == K:  result += 1
    print(f'#{t+1} {result}')