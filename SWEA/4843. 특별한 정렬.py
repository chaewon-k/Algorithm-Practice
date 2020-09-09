T = int(input())
for t in range(T):
    N = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort()
    result_list = []

    rangee = N//2 if N % 2 == 0 else N//2 + 1

    for i in range(rangee):
        j= N-i-1
        if i != j:
            result_list.append(input_list[j])
            result_list.append(input_list[i]) 
        else:
            result_list.append(input_list[i])

    print(f'#{t+1}', end = ' ')
    for i in range(10):
        print(result_list[i], end = ' ')
    print('')