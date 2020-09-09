def r_c_check(arr):
    r_list = [0]*9; c_list = [0]*9

    for i in range(9):
        for j in range(9):
            r_list[arr[i][j] - 1] += 1
            c_list[arr[j][i] - 1] += 1
        for j in range(9):
            if r_list[j] != 1 or c_list[j] != 1:
                return False
        r_list = [0]*9; c_list = [0]*9
    return True

def sqr_check(arr):
    num_list = [0]*9
    for i in range(3):
        start_r = i*3
        for j in range(3):
            start_c = j*3
            for x in range(start_r, start_r+3):
                for y in range(start_c, start_c+3):
                    num_list[arr[x][y]-1] += 1
            for k in range(9):
                if num_list[k] != 1:    return False
            num_list = [0]*9
    return True

T = int(input())
for t in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t+1}',end = ' ')
    if r_c_check(sudoku) == True and sqr_check(sudoku) == True:
        print("1")
    else:   print("0")