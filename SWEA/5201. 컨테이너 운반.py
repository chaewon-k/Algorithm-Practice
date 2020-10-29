T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    i = j = result = 0
    while i<M and j<N:
        if container[j] <= truck[i]:
            result += container[j]
            j += 1
            i += 1
        else:
            j += 1

    print(f'#{t} {result}')

