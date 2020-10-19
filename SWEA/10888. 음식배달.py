from itertools import combinations

T = int(input())
for t in range(T):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N)]
    home = []
    delivery = []

    for i in range(N):
        for j in range(N):
            if town[i][j] == 1: home.append([i, j])
            if town[i][j] >= 2: delivery.append([i, j])
    distance = []
    for i in delivery:
        temp = []
        for j in home:
            temp.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
        distance.append(temp)

    mini = 10000000
    # 1. 한 개의 식당만 선택할 경우
    for i in range(len(delivery)):
        temp = sum(distance[i]) + town[delivery[i][0]][delivery[i][1]]
        if mini > temp: mini = temp
    num_list = list(range(len(delivery)))

    # 2. 두 개 이상의 식당을 선택할 경우
    for r in range(2, len(delivery) + 1):
        combi = list(combinations(num_list, r))

        for com in combi:
            dist_list = []
            for j in range(len(home)):
                temp = 100000
                for i in com:
                    if temp > distance[i][j]:   temp = distance[i][j]
                dist_list.append(temp)

            summ = sum(dist_list)
            for k in com:
                summ += town[delivery[k][0]][delivery[k][1]]
            if mini > summ: mini = summ

    print(f'#{t + 1} {mini}')