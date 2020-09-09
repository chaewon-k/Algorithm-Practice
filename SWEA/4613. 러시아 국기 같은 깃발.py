T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    array =[input()for _ in range(n)]
    ans = n*m
    for i in range(n-2):
        for j in range(i+1, n-1):
            change = 0
            for r in range(i + 1):
                for c in range(m):
                    if array[r][c] != 'W': change += 1
            for r in range(i + 1, j + 1):
                for c in range(m):
                    if array[r][c] != 'B': change += 1
            for r in range(j + 1, n):
                for c in range(m):
                    if array[r][c] != 'R': change += 1
            ans = min(ans, change)
    print('#{} {}'.format(t+1, ans))