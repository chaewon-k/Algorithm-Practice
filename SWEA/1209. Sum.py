for t in range(10):
    T = int(input())
    
    my_list = []
    for i in range(100):
        my_list.append(list(map(int,input().split())))
    
    row_sum = col_sum = d1 = d2 = 0
    maxi = -1

    for i in range(100):
        for j in range(100):
            row_sum += my_list[i][j]
            col_sum += my_list[j][i]

            if i == j:  d1 += my_list[i][j]
            if i == (100-j-1):  d2 += my_list[i][j]

        if maxi < row_sum:  maxi = row_sum
        if maxi < col_sum:  maxi = col_sum
        
        row_sum = 0
        col_sum = 0
    
    if maxi < d1:   maxi = d1
    if maxi < d2:   maxi = d2

    print(f'#{T} {maxi}')