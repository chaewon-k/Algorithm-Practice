dirs = [(0,1),(1,0),(0,-1),(-1,0)]    # 0: 하, 1: 우, 2: 상, 3: 좌

def dfs(start, prev, N, board, count):
    if start[0] == start[1] == N-1:
        return

    for d in dirs:
        dx, dy = start[0] + d[0], start[1] + d[1]
        if 0 <= dx < N and 0 <= dy < N and board[dx][dy] == 0:
            if start[0] - prev[0] == dx - start[0] or start[1] - prev[1] == dy - start[1]:
                plus = 100
            else:
                plus = 600

            updated = count[start[0]][start[1]] + plus

            if updated <= count[dx][dy]:
                count[dx][dy] = updated
                dfs([dx,dy],start,N,board,count)
    return

def solution(board):
    N = len(board)
    count = [[float('inf')] * N for _ in range(N)]
    count[0][0] = 0
    dfs([0,0],[0,0],N,board,count)

    return count[-1][-1]

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))  # 2100

# bfs 풀이 (정석 풀이)
# def solution(board):
#     from collections import deque
#     length = len(board)
#     costs = [[float('inf')]*length for _ in range(length)]
#     costs[0][0] = 0
#     queue = deque([(0,0,0,0,0)])
#     while queue:
#         x, y, px, py, prev_cost = queue.popleft()
#         for dx, dy in dirs:
#             nx, ny = x + dx, y + dy
#             if 0<=nx<length and 0<=ny<length:
#                 if board[nx][ny] == 0:
#                     new_cost = prev_cost + (100 if x-px == nx-x or y-py == ny-y else 600)
#                     if new_cost <=costs[nx][ny]:
#                         costs[nx][ny] = new_cost
#                         queue.append((nx,ny,x,y,new_cost))
#     return costs[-1][-1]