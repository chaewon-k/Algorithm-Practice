T = int(input())

for t in range(T):
    N, M = map(int,input().split())
    carrot = list(map(int, input().split()))

    distance = 0
    max_weight = M
    i = 0

    while i < N:
        
        if max_weight <= carrot[i]:
            carrot[i] -= max_weight
            max_weight = M
            distance += (i+1)*2
        
        else:
            max_weight -= carrot[i]
            carrot[i] = 0
            i += 1
    distance += 2*N
    print(f'#{t+1} {distance}')

        
