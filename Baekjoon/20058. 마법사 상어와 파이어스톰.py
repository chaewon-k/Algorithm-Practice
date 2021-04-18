from collections import deque
def bfs(x, y):
    queue = deque([(x,y)])
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < arr_len and 0 <= dy < arr_len and arr[dx][dy] > 0 and not visited[dx][dy]:
                visited[dx][dy] = 1
                queue.append((dx,dy))
                cnt += 1
    return cnt

N, Q = map(int, input().split())
arr_len = 2**N
arr =[list(map(int, input().split())) for _ in range(arr_len)]
L = list(map(int, input().split()))

for q in range(Q):
    L_len = 2**L[q]
    #rotation
    for row_start in range(0,arr_len,L_len):
        row_end = row_start + L_len
        for col_start in range(0,arr_len,L_len):
            col_end = col_start + L_len
            sub_arr = [arr[i][col_start:col_end] for i in range(row_start,row_end)]
            for i in range(L_len):
                for j in range(L_len):
                    arr[row_start+j][col_start+L_len-1-i] = sub_arr[i][j]

    #melting count
    counting = [[0]*arr_len for _ in range(arr_len)]
    for i in range(arr_len):
        for j in range(arr_len):
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                di, dj = i+dx, j+dy
                if 0 <= di < arr_len and 0 <= dj < arr_len and arr[di][dj] > 0:
                    counting[i][j] += 1

    #discount_melting
    for i in range(0, arr_len):
        for j in range(0, arr_len):
            if arr[i][j] > 0 and counting[i][j] < 3:
                arr[i][j] -= 1

#Amount
amount = sum(sum(i) for i in arr)

#dfs
maxi = 0
visited = [[0]*arr_len for _ in range(arr_len)]
for i in range(arr_len):
    for j in range(arr_len):
        if arr[i][j] and visited[i][j] == 0:
            visited[i][j] = 1
            maxi = max(maxi, bfs(i, j))

print(amount)
print(maxi)
