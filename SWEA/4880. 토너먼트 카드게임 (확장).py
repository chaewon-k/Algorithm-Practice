def Queue(queue, idx_list, ct):
    while True:
        if ct == 1:
            temp = queue.pop(0)
            queue.append(temp)
            temp2 = idx_list.pop(0)
            idx_list.append(temp2)
            ct = len(queue)
        if ct == 0:     ct = len(queue)
        if len(queue) == 1:     return idx_list[0]
        else:
            a, b = queue.pop(0), queue.pop(0)
            a_idx, b_idx = idx_list.pop(0), idx_list.pop(0)
            ct -= 2
            if a > b:
                if a == 3 and b == 1:
                    queue.append(b)
                    idx_list.append(b_idx)
                else:
                    queue.append(a)
                    idx_list.append(a_idx)
            elif a < b:
                if a == 1 and b == 3:
                    queue.append(a)
                    idx_list.append(a_idx)
                else:
                    queue.append(b)
                    idx_list.append(b_idx)
            else:
                queue.append(a)
                idx_list.append(a_idx)

T = int(input())
for t in range(T):
    N = int(input())
    members = list(map(int,input().split()))

    queue1, queue2 = members[:(N//2)], members[(N//2):]
    idx1, idx2 = list(range(N//2)), list(range(N//2, N))
    cnt = len(queue1)
    x = Queue(queue1, idx1, cnt)
    cnt = len(queue2)
    y = Queue(queue2, idx2, cnt)
    result = 0

    if members[x] > members[y]:
        if members[x] == 3 and members[y] == 1:     result = y+1
        else:   result = x+1

    elif members[x] < members[y]:
        if members[x] == 3 and members[y] == 1:     result = x+1
        else:   result = y+1

    else:   result = min(x,y)+1

    print(f'#{t+1} {result}')




