delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
def cancel(row, col, dir, plus):
    dr, dc = delta[dir]
    for _ in range(plus):
        board[row + dr][col + dc] = 0
        row += dr
        col += dc


def install(row, col, dir):
    srow = row
    scol = col
    dr, dc = delta[dir]
    plus = 0
    while 0 <= row + dr < N and 0 <= col + dc < N:
        row += dr
        col += dc
        if board[row][col]:
            break
        board[row][col] = 1
        plus += 1
    else:
        return plus
    cancel(srow, scol, dir, plus)
    return 0


def DFS(now, last, code):
    global maxCores, minCode
    if maxCores < len(now):
        maxCores = len(now)
        minCode = 12 * 12 + 1
    if maxCores == len(now) and minCode > code:
        minCode = code

    for i in range(last, len(cores)):
        for dir in range(4):
            plus = install(*cores[i], dir)
            if not plus:
                continue
            next = now[:]
            next.append(i)
            DFS(next, i + 1, code + plus)
            cancel(*cores[i], dir, plus)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j] == 1:  cores.append((i,j))

    maxCores = -1
    minCode = 12 * 12 + 1
    DFS([], 0, 0)
    print('#%d' % test_case, minCode)