def find(array):
    global arr_len, N, M
    for k in range(arr_len-1, 0, -1):
        for i in range(0, arr_len-k+1,1):
            for j in range(0, arr_len-k+1,1):
                temp_arr = array[:]
                for m in range(i, i+k):
                    for n in range(j, j+k):
                        temp_arr[m][n] = 0
                for m in range(arr_len):
                    for n in range(arr_len):
                        if temp_arr[m][n] > 0:
                            ## 여기가 문제



def swap(li):
    temp = li[0]
    li[0] = li[2]
    li[2] = temp
    temp = li[1]
    li[1] = li[3]
    li[3] = temp
    return li

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    idx_list = [list(map(int, input().split())) for _ in range(N)]
    arr_len = 0
    for idx in idx_list:
        if max(idx) > arr_len:
            arr_len = max(idx)

        if idx[0] > idx[2]:
            idx = swap(idx)
        elif idx[0] == idx[2]:
            if idx[1] > idx[3]:
                idx = swap(idx)
    idx_list.sort(key= lambda x: x[0])

    arr = [[0]*(arr_len+1) for _ in range(arr_len+1)]
    arr_len += 1
    mem_list = {}

    for idx in idx_list:
        if idx[1] <= idx[3]:
            for i in range(idx[0], idx[2]):
                for j in range(idx[1], idx[3]):
                    arr[i][j] += 1
                    mem_list[(i,j)] = 0
        else:
            for i in range(idx[0], idx[2]):
                for j in range(idx[1], idx[3], -1):
                    arr[i][j] += 1
                    mem_list[(i,j)] = 0

    print(f'#{t+1} {find(arr)}')

#
# 1
# 5 1
# 7 2 5 8
# 4 7 6 6
# 4 4 3 3
# 0 1 3 3
# 1 0 4 2
#
# k = 7