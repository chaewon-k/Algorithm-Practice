T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    time_list = list(map(int, input().split()))
    time_list.sort()
    result = 'Possible'
    K_temp = j = 0
    for i in range(time_list[-1]+1):
        if i%M == 0 and i != 0:
            K_temp += K
        if i == time_list[j]:
            if K_temp > 0:
                j += 1
                K_temp -= 1
            else:
                result = 'Impossible'
                break
    print('#{} {}'.format(t+1, result))
