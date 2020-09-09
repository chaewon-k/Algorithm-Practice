T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Pizza = list(map(int, input().split()))
    queue = list(range(N))
    while len(queue):
        pizza = queue.pop(0)
        Pizza[pizza] //= 2
        if Pizza[pizza] != 0:   queue.append(pizza)
        else:
            if N < M:
                queue.append(N)
                N += 1

    print(f'#{t} {pizza+1}')