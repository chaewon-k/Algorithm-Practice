N = int(input())
arr = list(map(int, input().split()))

cnt = 1
result = []
for i in range(1,len(arr)):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        result.append(cnt)
        cnt = 1
cnt = 1
result.append(cnt)

for i in range(1,len(arr)):
    if arr[i-1] >= arr[i]:
        cnt += 1
    else:
        result.append(cnt)
        cnt = 1
result.append(cnt)

print(max(result))