T = int(input())

for t in range(T):
    N = int(input())
    my_list = list(map(int, input().split()))
    sum_list = []
    for i in range(N-1):
        summ = my_list[i]+my_list[i+1]
        sum_list.append(summ)

    print(f'#{t+1} {max(sum_list)} {min(sum_list)}')