def sub_list_sum(arr, length, summ):
    cnt = 0
    total_sub_list = []
    for i in range(1 << 12):
        sub_list = []
        for j in range(12):
            if i & (1 << j):    sub_list.append(arr[j])
        total_sub_list.append(sub_list)

    for i in total_sub_list:
        if sum(i) == summ and len(i) == length : cnt += 1
    return cnt
    
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    my_list = []
    for i in range(12):
        my_list.append(i+1)
    
    print(f'#{t+1} {sub_list_sum(my_list, N, K)}')