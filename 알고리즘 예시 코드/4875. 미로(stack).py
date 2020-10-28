for tc in range(1, int(input()) + 1):
    n = int(input())
    maze = []

    for _ in range(n):
        maze.append(input())
        if '2' in maze[-1]:
            x, y = len(maze) - 1, maze[-1].index('2')
            stack = [(x, y)]

    v = [[0] * (n + 1) for _ in range(n + 1)]
    d = [0, 1, 0, -1, 0]
    ans = 0

    while stack:
        x, y = stack.pop()
        if maze[x][y] == '3':
            ans = 1
            break
        v[x][y] = 1
        for i in range(4):
            dx, dy = x + d[i], y + d[i + 1]
            if 0 <= dx < n and 0 <= dy < n and maze[dx][dy] != '1' and not v[dx][dy]:
                stack.append((dx, dy))

    print(f'#{tc} {ans}')