N = int(input())
arr = [[0]*101 for _ in range(101)]
for n in range(N):
    x,y,r,c = map(int, input().split())

    for i in range(x, x+r):
        for j in range(y,y+c):
            arr[i][j] = n+1
result = [0]*N
for n in range(1, N+1):
    for i in range(101):
        for j in range(101):
            if arr[i][j] == n:
                result[n-1] += 1
for i in result:
    print(i)

