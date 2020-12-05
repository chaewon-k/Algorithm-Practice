def choose(r,c):
    global first, second
    honey = arr[r][c:c+M]
    max_cost = 0

    for i in range(1<<N):
        sum_honey = sum_cost = 0
        for j in range(M):
            if i & (1<<j):
                sum_honey += honey[j]
                sum_cost += honey[j] ** 2
        if sum_honey <= C:
            max_cost = max(max_cost, sum_cost)

    if max_cost > first[0]:
        if r == first[1] and c < first[2] + M:
            first = [max_cost,r,c]
        else:
            second = first[:]
            first = [max_cost,r,c]
    elif max_cost > second[0]:
        if r != first[1] or c >= first[2] + M:
            second = [max_cost,r,c]


for t in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    first = [0,0,0]
    second = [0,0,0]

    for i in range(N):
        for j in range(N-M+1):
            choose(i,j)

    print(f'#{t} {first[0]+second[0]}')