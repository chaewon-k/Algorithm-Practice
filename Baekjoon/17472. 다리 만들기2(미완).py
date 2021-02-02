def BFS(visited):
    num = 1
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and visited[r][c] == 0:
                queue = []
                queue.append([r,c])
                visited[r][c] = num
                while queue:
                    x, y = queue.pop(0)
                    for dx,dy in dir:
                        new_x, new_y = x+dx, y+dy
                        if 0 <= new_x < N and 0 <= new_y < M and arr[new_x][new_y] == 1 and not visited[new_x][new_y]:
                            queue.append([new_x,new_y])
                            visited[new_x][new_y] = num
                num += 1
    return visited, num

def find_bridge(bridge, country):
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:


dir = [[0,-1],[0,1],[1,0],[-1,0]]
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

country_num, num = BFS(visited)

bridge = [[0]*num for _ in range(num)]
find_bridge(bridge, country_num)

