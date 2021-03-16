from itertools import product
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    person = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                person.append((i,j))
            elif arr[i][j] > 0:
                stairs.append((i,j,arr[i][j]))

    dists = []
    for i in person:
        temp = []
        for j in stairs:
            temp.append(abs(i[0] - j[0]) + abs(i[1] - j[1]) + j[2])
        dists.append(temp)

    comb = list(product(range(len(stairs)),repeat=len(person)))
    print(comb)

    for com in comb:
        stair_1 = []
        stair_2 = []
        for c in range(len(com)):
            if com[c] == 0:
                stair_1.append(dists[c][0])
            else:
                stair_2.append(dists[c][1])
        stair_1.sort()
        stair_2.sort()

        queue = []
        while stair_1:
            if len(queue) == 3:
                if queue[2] == stair_1[0]:

            else:
                queue.append(stair_1.pop(0))


