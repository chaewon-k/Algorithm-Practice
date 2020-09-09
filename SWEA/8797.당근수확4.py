T = int(input())

for t in range(T):
    N = int(input())

    carrot = []
    for i in range(N):
        carrot.append(list(map(int,input().split())))
    sum_list = [0]*4

    for i in range(N):
        for j in range(N):
            if i<j and i+j<N-1: sum_list[0] += carrot[i][j]
            if i>j and i+j<N-1: sum_list[1] += carrot[i][j]
            if i<j and i+j>N-1: sum_list[2] += carrot[i][j]
            if i>j and i+j>N-1: sum_list[3] += carrot[i][j]

    print(f'#{t+1} {max(sum_list)-min(sum_list)}')    
