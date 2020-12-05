def solution(board):
    answer = 25*25*500
    temp = 0
    N = len(board)
    queue = []
    queue.append((0,0,-1))
    visited = [[0]*N for _ in range(N)]
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    while queue:
        x, y, flag = queue.pop(0)
        if x == y == N-1:
            if temp < answer:
                answer = temp
        visited[x][y] = 1
        for d in range(4):
            dx, dy = x+dirs[d][0], y+dirs[d][1]
            if 0<=dx<N and 0<=dy<N and not visited[dx][dy] and board[dx][dy] == 0:
                if flag == -1:
                    temp += 100
                    flag = d
                else:
                    if flag != d:
                        flag = d
                        temp += 500
                    else:
                        temp += 100
                queue.append((dx,dy,flag))
            print(queue)




    print(answer)

solution([[0,0,0],[0,0,0],[0,0,0]])
