T = int(input())

for t in range(T):
    N, M = map(int,input().split())
    aj = list(map(int, input().split()))

    maximum = minimum = sum(aj[0:M])

    for i in range(N-M+1):
        temp = sum(aj[i:i+M])

        if maximum < temp:
            maximum = temp
        if minimum > temp:
            minimum = temp

    print(f'#{t+1} {maximum-minimum}')