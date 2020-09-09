T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    word_table = [[0]*3 for _ in range(N)]
    mini = 100000000

    for i in range(N):
        word_table[i][0] = arr[i].count('W')
        word_table[i][1] = arr[i].count('B')
        word_table[i][2] = arr[i].count('R')

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            count = 0
            for k in range(i + 1):
                count += word_table[k][1] + word_table[k][2]
            for k in range(i + 1, j + 1):
                count += word_table[k][0] + word_table[k][2]
            for k in range(j + 1, N):
                count += word_table[k][0] + word_table[k][1]
            if mini > count:    mini = count

    print(f'#{t+1} {mini}')
