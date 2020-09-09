def check(arr, x, y):
    row_cnt = col_cnt = 1
    temp_x = x + 1; temp_y = y + 1
    
    while temp_x < N:
        if arr[temp_x][y] != 0:    
            row_cnt += 1
            temp_x += 1
        else:   break
    
    while temp_y < N:
        if arr[x][temp_y] != 0:
            col_cnt += 1
            temp_y += 1
        else:   break

    for m in range(x, temp_x):
        for n in range(y, temp_y):
            arr[m][n] = 0

    return temp_x - x, temp_y - y

def selection_sort(a,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[2][min_idx] > a[2][j]:
                min_idx = j
                print(j)
            elif a[2][j] == a[2][min_idx]:
                if a[0][j] < a[0][min_idx]:
                    min_idx = j

        a[2][i], a[2][min_idx] = a[2][min_idx], a[2][i]
        a[1][i], a[1][min_idx] = a[1][min_idx], a[1][i]
        a[0][i], a[0][min_idx] = a[0][min_idx], a[0][i]

    
    return a    

T = int(input())
for t in range(T):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    r_arr = []; c_arr = []; area = []

    for i in range(N):
        for j in range(N):
            if array[i][j] != 0:
                row , col = check(array, i, j)
                r_arr.append(row)
                c_arr.append(col)

    result_arr = [[0]*len(r_arr) for _ in range(3)]

    for i in range(len(r_arr)):
        result_arr[0][i] = r_arr[i]
        result_arr[1][i] = c_arr[i]
        result_arr[2][i] = r_arr[i] * c_arr[i]

    print(selection_sort(result_arr, len(r_arr)))

    # print(f'#{t+1} {len(r_arr)}', end = ' ')
    # for i in range(len(r_arr)):
    #     print(f'{result_arr[0][i]} {result_arr[1][i]}', end = ' ')
    # print('')
