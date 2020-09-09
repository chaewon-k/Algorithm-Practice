T = int(input())
for t in range(T):
    N = int(input())
    carrot = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0; x_list = []; y_list = []; y_flag = 1

    for i in range(N):
        for j in range(N):
            if carrot[i][j] == 1:
                x_list.append(i); y_list.append(j)
                y_flag *= -1

    start_x = x_list[0]; start_y = y_list[0]; temp_cnt = 1
    for i in range(start_x,N):
        for j in range(start_y,N):
            if carrot[i][j] == 0:
                x_list.append(i)
                y_list.append(j-1)
                break
        if carrot[i][j] == 0:
            x_list.append(i-1)
            y_list.append(j-1)
            break

    x_list.append(j-1)
    y_list.append(i-1)
    print(x_list)
    print(y_list)
    cnt = 0
    for m in range(x_list[0]+1):
        for n in range(y_list[0]+1):
            if carrot[m][n] == 2:   cnt += 1
    for m in range(x_list[1] + 1):
        for n in range(y_list[1], N):
            if carrot[m][n] == 2:   cnt += 1
    for m in range(x_list[2],N):
        for n in range(y_list[2]+1):
            if carrot[m][n] == 2:   cnt += 1
    for m in range(x_list[3],N):
        for n in range(y_list[3],N):
            if carrot[m][n] == 2:   cnt += 1

    print(f'#{t+1} {cnt}')