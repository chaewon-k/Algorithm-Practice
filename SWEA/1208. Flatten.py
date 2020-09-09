for t in range(10):
    dump = int(input())
    box_list = list(map(int,input().split()))

    for i in range(dump):
        maximum = max(box_list)
        minimum = min(box_list)
        idx_max = box_list.index(maximum)
        idx_min = box_list.index(minimum)
        box_list[idx_max] -= 1
        box_list[idx_min] += 1

    diff = max(box_list) - min(box_list)
    print(f'#{t+1} {diff}')