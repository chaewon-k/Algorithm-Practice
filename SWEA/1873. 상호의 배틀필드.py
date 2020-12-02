# import sys
# sys.stdin = open("input.txt", "r")

tank = ['^','v','<','>']
dir_dict = {'U':0, 'D':1, 'L':2, 'R':3}

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def search_tank():
    for i in range(H):
        for j in range(W):
            if game[i][j] in tank:
                return i, j, tank.index(game[i][j])

T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    game = [list(input()) for _ in range(H)]
    N = int(input())
    cmd_list = list(input())

    # 1. 탱크 위치를 찾기
    r = c = dir = -1
    r,c,dir = search_tank()

    # 2. 명령어 처리
    # 2-1.포탄 발사를 할 때
    for cmd in cmd_list:
        if cmd == 'S':
            nr = r+dr[dir]
            nc = c+dc[dir]
            
            while 0<=nr<H and 0<=nc<W:
                if game[nr][nc] == '#': break
                if game[nr][nc] == '*':
                    game[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]
                
        # 2-2. 방향을 조종할 때
        else:
            dir = dir_dict[cmd]
            # 전차 방향 바꾸기
            game[r][c] = tank[dir]
            
            nr = r+dr[dir]
            nc = c+dc[dir]
            
            if 0<=nr<H and 0<=nc<W and game[nr][nc] == '.':
                game[nr][nc] = tank[dir]
                game[r][c] = '.'
                r,c = nr,nc  # r,c 현재 탱크의 위치

    # 3. 출력
    print(f'#{t}', end = ' ')

    for i in range(H):
        for j in range(W):
            print(game[i][j], end='')


