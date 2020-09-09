def Ladder(row, col):
    cnt = 0
    while row > 0:
        i = row
        if col - 1 >= 0 and ladder[i][col - 1] == 1:
            for j in range(col - 1, -1, -1):
                cnt += 1
                if ladder[row - 1][j] == 1:
                    col = j
                    break
        elif col + 1 <= 99 and ladder[i][col + 1] == 1:
            for j in range(col + 1, 100):
                cnt += 1
                if ladder[row - 1][j] == 1:
                    col = j
                    break
        i -= 1
        cnt += 1
    return cnt

for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    row = 99
    shortest = 1000000000000000
    result = -1
    col_list = []
    for i in range(100):
        if ladder[row][i] == 1:
            col = i
            i = row = 99
            count = Ladder(row,col)
            if shortest > count:
                shortest = count
                result = col

    print(f'#{t} {result}')