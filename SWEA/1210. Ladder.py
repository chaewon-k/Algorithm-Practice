for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    row = 99
    for i in range(100):
        if ladder[row][i] == 2:
            col = i
            break
    i = row
    while row > 0:
        row = i
        if col-1 >= 0 and ladder[i][col-1] == 1:  #왼쪽에 길이 있을 때
            for j in range(col-1,-1,-1): #왼쪽으로 이동
                if ladder[row-1][j] == 1: #윗쪽으로 길이 있다면
                    col = j
                    break
        elif col+1 <= 99 and ladder[i][col+1] == 1: #오른쪽에 길이 있을 때
            for j in range(col+1, 100):
                if ladder[row-1][j] == 1:
                    col = j
                    break
        i -= 1
    print(f'#{t} {col}')