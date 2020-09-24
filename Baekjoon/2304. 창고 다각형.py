N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
maxi = arr[-1][0]
Map = [0]*(maxi+1)
for i in arr:
    Map[i[0]] = i[1]
result = max(Map)
total_max = max(Map)
i = Map.index(max(Map))
while 0<=i:         # 가장 높은 기둥의 왼쪽
    temp = Map[:i]
    if len(temp) == 0:
        break
    left_max = max(temp)
    if left_max == 0:
        break
    idx = Map.index(left_max)
    result += left_max*(i - idx)
    i = idx
    total_max = left_max

total_max = max(Map)
i = Map.index(max(Map))
while i <= maxi:         # 가장 높은 기둥의 왼쪽
    temp = Map[i+1:]
    if len(temp) == 0:
        break
    right_max = max(temp)
    if right_max == 0:
        break
    idx = Map.index(right_max)
    result += right_max*(idx - i)
    i = idx
    total_max = right_max

print(result)