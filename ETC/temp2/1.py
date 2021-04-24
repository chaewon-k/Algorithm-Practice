from collections import deque
from copy import deepcopy
def plus(turn):
    global soldier
    update_soldier = deepcopy(soldier)

    for i in range(N):
        for j in range(N):
            queue = deque()
            if area[i][j] == turn:
                case = 0
                for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx, dy = i + d[0], j + d[1]
                    if 0<=dx < N and 0<=dy<N and area[dx][dy] != turn and area[dx][dy] != 0:
                        case = 1
                    else:
                        queue.append((dx,dy))
                if case == 0:   # 사방이 아군
                    while queue:
                        x, y = queue.popleft()
                        if 0<=x<N and 0<=y<N and soldier[x][y] != 0:
                            update_soldier[x][y] += plus_soldier[i][j]
                            update_soldier[i][j] -= plus_soldier[i][j]
                else:       # 하나 이상 적군
                    while queue:
                        x, y = queue.popleft()
                        if 0 <= x < N and 0 <= y < N and soldier[x][y] != 0:
                            if soldier[i][j] > 5 * soldier[x][y]:
                                update_soldier[x][y] += plus_soldier[i][j]
                                update_soldier[i][j] -= plus_soldier[i][j]
    soldier = deepcopy(update_soldier)

def attack(turn):
    global soldier
    # 공격해서 다른 나라 차지하기
    update_soldier = deepcopy(soldier)
    for i in range(N):
        for j in range(N):
            if area[i][j] != 0 and area[i][j] != turn:
                queue = deque()
                ssum = 0
                for d in [(-1,0), (1,0), (0,-1), (0,1)]:
                    dx, dy = i+d[0], j+d[1]
                    if 0<= dx < N and 0<=dy<N and area[dx][dy] == turn:
                        queue.append((dx,dy))
                        ssum += soldier[dx][dy]
                if ssum > soldier[i][j] * 5:
                    area[i][j] = turn
                    diff_sum = 0
                    while queue:
                        x, y = queue.popleft()
                        update_soldier[x][y] -= new_soldier[x][y]
                        diff_sum += new_soldier[x][y]
                    update_soldier[i][j]  = diff_sum - update_soldier[i][j]
    # 한번에 다 빼주기
    soldier = deepcopy(update_soldier)


for t in range(int(input())):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    soldier = [list(map(int, input().split())) for _ in range(N)]
    add_soldier = [list(map(int, input().split())) for _ in range(N)]
    new_soldier = [[0]*N for _ in range(N)]
    plus_soldier = [[0]*N for _ in range(N)]
    remain_area = [0,1,1,1]
    turn = 1

    while True:
        if remain_area[turn] == 1:       # 살아 있을 때
            remain_soldier = [0, 0, 0, 0]
            remain_area = [0,0,0,0]
            # 공격시 사용할 지원 수 배열
            for i in range(N):
                for j in range(N):
                    new_soldier[i][j] = soldier[i][j] // 4
            # 종료조건 (한 나라만 남으면)
            # 1. 공격
            attack(turn)
            # 2. 지원
            for i in range(N):
                for j in range(N):
                    plus_soldier[i][j] = soldier[i][j] // 5
            plus(turn)
            # 3. 보충
            for i in range(N):
                for j in range(N):
                    soldier[i][j] += add_soldier[i][j]

            # 남은 나라 수 세기
            for i in range(N):
                for j in range(N):
                    remain_area[area[i][j]] = 1
                    remain_soldier[area[i][j]] += soldier[i][j]
            remain_area[0] = 0
            if sum(remain_area) == 1:
                print(f'# {t+1} {sum(remain_soldier)}')
                break
        # print(area)
        turn += 1
        if turn > 3:
            turn = 1