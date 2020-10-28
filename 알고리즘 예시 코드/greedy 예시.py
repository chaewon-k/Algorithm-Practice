# 0-1 knapsack

N, K = map(int, input().split())    # 물건의 개수와 담을 수 있는 최대 무게
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])

# 핵심 알고리즘
# dp [i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]])
# 현재 물건을 안 넣은 경우 // 현재 물건을 넣은 경우, 현재 물건을 넣기 전의 최대 가치+현재 물건의 가치
