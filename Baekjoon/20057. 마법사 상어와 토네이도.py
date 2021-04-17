import sys

def storm(x, y, sand):
    global ans
    if 0 <= x < n and 0 <= y < n:
        a[x][y] += sand
    else:
        ans += sand

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2

i, cnt, ans, move, turn = 0, 0, 0, 0, 1
while True:
    nx = x + dx[i]
    ny = y + dy[i]
    if a[nx][ny]:
        _1 = int(a[nx][ny] * 0.01)
        _2 = int(a[nx][ny] * 0.02)
        _7 = int(a[nx][ny] * 0.07)
        _5 = int(a[nx][ny] * 0.05)
        _10 = int(a[nx][ny] * 0.1)
        rem = a[nx][ny] - 2 * (_1 + _2 + _7 + _10) - _5

        _1x_u, _1y_u = x + dx[(i + 3) % 4], y + dy[(i + 3) % 4]
        _1x_d, _1y_d = x + dx[(i + 1) % 4], y + dy[(i + 1) % 4]
        _2x_u, _2y_u = nx + 2 * dx[(i + 3) % 4], ny + 2 * dy[(i + 3) % 4]
        _2x_d, _2y_d = nx + 2 * dx[(i + 1) % 4], ny + 2 * dy[(i + 1) % 4]
        _7x_u, _7y_u = nx + dx[(i + 3) % 4], ny + dy[(i + 3) % 4]
        _7x_d, _7y_d = nx + dx[(i + 1) % 4], ny + dy[(i + 1) % 4]

        tx, ty = nx + dx[i], ny + dy[i]
        _10x_u, _10y_u = tx + dx[(i + 3) % 4], ty + dy[(i + 3) % 4]
        _10x_d, _10y_d = tx + dx[(i + 1) % 4], ty + dy[(i + 1) % 4]
        _5x, _5y = tx + dx[i], ty + dy[i]

        storm(tx, ty, rem)
        storm(_1x_u, _1y_u, _1)
        storm(_1x_d, _1y_d, _1)
        storm(_2x_u, _2y_u, _2)
        storm(_2x_d, _2y_d, _2)
        storm(_7x_u, _7y_u, _7)
        storm(_7x_d, _7y_d, _7)
        storm(_10x_u, _10y_u, _10)
        storm(_10x_d, _10y_d, _10)
        storm(_5x, _5y, _5)

    if x == 0 and y == 0:
        break

    a[nx][ny] = 0
    x, y = nx, ny
    cnt += 1
    if cnt == turn:
        i = (i + 1) % 4
        cnt = 0
        move += 1
        if move % 2 == 0:
            turn += 1
            move = 0

print(ans)