def down(idx):
    group = []
    cnt = 1
    num = 1
    for row in range(1,N):
        if arr[row][idx] == num:
            cnt += 1
        else:
            group.append((row-cnt,cnt))
            cnt = 1
            num = arr[row][idx]
    group.append([row-cnt+1,cnt])

    print(group)

    prev = group[0]
    force = group[0][1]
    for i in range(1, len(group)):
        if i % 2 == 0:  #1블럭일 때
            # 더 큰 힘으로 누를 때
            if force > group[i][1]:
                force += group[i][1]
                prev[1] += group[i][1]
            else:
                break

        else:   # 0 블럭일 때
            force *= (1.9)**group[i][1]

            # 이동
            for j in range(prev[0], prev[0]+prev[1]):
                arr[j][idx] = 0

            end = group[i][0] + group[i][1]-1
            for j in range(end, end-prev[1], -1):
                arr[j][idx] = 1
            prev = [end-prev[1]+1, prev[1]]
        print(arr)



for t in range(1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for col in range(N):
        if arr[0][col] == 1:
            down(col)
            break
    # print(arr)