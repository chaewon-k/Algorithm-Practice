T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[0 for _ in range(3)] for _ in range(N)]

    temp = ''
    for i in range(N):
        for j in range(N - 1, -1, -1):
            temp += str(arr[j][i])
        result[i][0] = temp
        temp = ''

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            temp += str(arr[i][j])
        result[N - i - 1][1] = temp
        temp = ''

    for i in range(N - 1, -1, -1):
        for j in range(N):
            temp += str(arr[j][i])
        result[N - 1 - i][2] = temp
        temp = ''

    print(f'#{t+1}')
    for k in range(N):
        print(' '.join(map(str, result[k])))