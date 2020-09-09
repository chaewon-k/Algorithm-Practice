T = int(input())
for t in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    masking = [0]*10001
    masking[0] = 1
    sum_list = [0]
    for i in scores:
        for j in range(len(sum_list)):
            if masking[sum_list[j] + i] == 0:
                masking[sum_list[j] + i] = 1
                sum_list.append(sum_list[j] + i)

    print(f'#{t+1} {len(sum_list)}')
