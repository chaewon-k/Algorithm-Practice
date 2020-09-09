import itertools

T = int(input())
for t in range(T):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    num_food = [i for i in range(N)]
    subset = list(itertools.combinations(num_food, N//2))
    diff = 100000
    for i in range(len(subset)//2):
        sub = list(itertools.combinations(subset[i],2))
        a_sum = b_sum = 0
        for j in sub:
            x, y = j
            a_sum += (food[x][y] + food[y][x])
        sub = list(itertools.combinations(subset[len(subset)-i-1], 2))
        for j in sub:
            x, y = j
            b_sum += (food[x][y] + food[y][x])
        temp_diff = abs(a_sum - b_sum)
        if diff > temp_diff:
            diff = temp_diff
    print(f'#{t+1} {diff}')