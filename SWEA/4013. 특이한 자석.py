def rot(mag, idx, flag):
    if flag == 1:
        end = mag[idx].pop()
        mag[idx].insert(0, end)
    else:
        end = mag[idx].pop(0)
        mag[idx].append(end)

T = int(input())
for t in range(T):
    K = int(input())
    mag = [list(map(int,input().split())) for _ in range(4)]
    rotation = [list(map(int, input().split())) for _ in range(K)]

    for r in rotation:
        dir = []
        idx = r[0]-1
        flag_ = r[1]
        dir.append([idx,flag_])
        for i in range(idx-1,-1,-1):
            if mag[i][2] == mag[i+1][6]:    break
            flag_ *= -1
            dir.append([i,flag_])

        flag_ = r[1]
        for i in range(idx + 1, 4):
            if mag[i][6] == mag[i - 1][2]:  break
            flag_ *= -1
            dir.append([i,flag_])

        for d in dir:
            rot(mag, d[0],d[1])

    result = 0
    for i in range(4):
        result += mag[i][0] * 2**i
    print(f'#{t+1} {result}')