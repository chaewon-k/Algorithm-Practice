T = int(input())
for t in range(T):
    N = int(input())
    array = [[0]*10 for _ in range(10)]

    for num in range(N):
        color_list = list(map(int, input().split()))

        for i in range(color_list[0], color_list[2]+1):
            for j in range(color_list[1], color_list[3]+1):
                if array[i][j] == 0 or array[i][j] != color_list[4]:
                    array[i][j] += color_list[4]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if array[i][j] == 3: cnt += 1
    print(f'#{t+1} {cnt}')
