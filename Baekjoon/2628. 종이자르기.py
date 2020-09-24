row, col = map(int, input().split())
N = int(input())
hori= [0]; vert = [0]
for n in range(N):
    a, b = map(int, input().split())
    if a == 0:  hori.append(b)
    else:   vert.append(b)
hori.append(col); vert.append(row)
hori.sort(); vert.sort()

hori_ = []; vert_ = []
length = len(hori)
for i in range(1, length):
    hori_.append(hori[i]-hori[i-1])
length = len(vert)
for i in range(1, length):
    vert_.append(vert[i]-vert[i-1])

print(max(hori_) * max(vert_))




