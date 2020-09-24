N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
num = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
maxi = -1
for i in range(6):
    result = 0
    k = dice[0][i]
    for d in dice:
        idx = d.index(k)
        next = num[idx]
        temp = []
        for j in range(len(d)):
            if j == idx or j == next:   continue
            else:   temp.append(d[j])
        result += max(temp)
        k = d[next]
    if maxi < result:   maxi = result
print(maxi)

