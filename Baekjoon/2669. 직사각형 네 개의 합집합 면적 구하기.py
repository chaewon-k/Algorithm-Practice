li = [list(map(int, input().split())) for _ in range(4)]
maxi = -1
for i in li:
    if maxi < max(i):
        maxi = max(i)

Map = [[0]*maxi for _ in range(maxi)]
for i in li:
    for x in range(i[0],i[2]):
        for y in range(i[1],i[3]):
            Map[x][y] += 1

area = 0
for i in range(maxi):
    for j in range(maxi):
        if Map[i][j] != 0:
            area += 1
print(area)