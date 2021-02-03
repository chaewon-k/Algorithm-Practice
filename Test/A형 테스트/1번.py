import itertools
T = int(input())
for test_case in range(1, T + 1):
    result = 10000000
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mem_list = []
    door_list = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  mem_list.append([i,j])
            elif arr[i][j] == 2:    door_list.append([i,j])

    dist = []
    for i in mem_list:
        temp = []
        for j in door_list:
            temp.append(abs(i[0]-j[0]) + abs(i[1]-j[1]))
        dist.append(temp)
    idx_list = list(itertools.product([0,1],repeat=len(mem_list)))

    for idx in idx_list:
        temp0 = {}; temp1 = {}; time0 = []; time1 = []

        for i in range(len(mem_list)):
            d = dist[i][idx[i]]
            if idx[i] == 0:
                if d not in temp0:
                    temp0[d] = 1
                else:
                    temp0[d] += 1
                time0.append(d+temp0[d])

            else:
                if d not in temp1:
                    temp1[d] = 1
                else:
                    temp1[d] += 1
                time1.append(d + temp1[d])
        time0.sort()
        time1.sort()
        for i in range(1, len(time0)):
            if time0[i] <= time0[i-1]:
                time0[i] = time0[i-1] + 1
        for i in range(1, len(time1)):
            if time1[i] <= time1[i-1]:
                time1[i] = time1[i-1] + 1

        temp_result = 0
        if len(time0) == 0:
            temp_result = time1[-1]
        elif len(time1) == 0:
            temp_result = time0[-1]
        else:
            temp_result = max(time0[-1], time1[-1])

        if temp_result < result:
            result = temp_result

    print(f'#{test_case} {result}')
    # 4,5,7,19,7


