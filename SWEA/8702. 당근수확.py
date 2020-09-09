T = int(input())

for t in range(T):
    N = int(input())
    carrot = list(map(int, input().split()))

    i_list = carrot[0]
    j_list = carrot[N-1]
    min_diff = 100
    last_index = 0
    i = 0
    j = N-1

    while i < j and i+1 != j:

        if i_list >= j_list:
            j_list += carrot[j-1]
            j -= 1

        else:
            i_list += carrot[i+1]
            i += 1
        
        diff = abs(i_list-j_list)

    print(f'#{t+1} {i+1} {diff}')