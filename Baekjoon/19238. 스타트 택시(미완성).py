def dfs(start, dest, arr_visited, cnt):
    if cnt > battery:
        return -1
    if start[0] == dest[0] and start[1] == dest[1]:
        return cnt

    for d in [(-1,0), (1,0), (0,-1), (0,1)]:
        dx, dy = start[0] + d[0], start[1] + d[1]
        if 0<=dx<N and 0<=dy<N and arr_visited[dx][dy] == 0 and arr[dx][dy] != 1:
            arr_visited[dx][dy] = 1
            dfs((dx, dy), dest, arr_visited, cnt + 1)
            arr_visited[dx][dy] = 0
    return

N, M, battery = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
arr_visited = [[0]*N for _ in range(N)]
info_visited = [0]*M
x -= 1
y -= 1
for i in infos:
    i[0] -= 1
    i[1] -= 1
    i[2] -= 1
    i[3] -= 1
cnt = 0

print(dfs((x,y), (1,1), arr_visited, 0))
# while cnt < M:
#
#     for info in infos:
#         dfs((x,y),(info[0],info[1]),arr_visited, 0)