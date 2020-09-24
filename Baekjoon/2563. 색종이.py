N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*101 for _ in range(101)]

for i in li:
    x,y = i
    for m in range(x,x+10):
        for n in range(y, y+10):
            board[m][n] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if board[i][j] != 0:
            cnt += 1
print(cnt)