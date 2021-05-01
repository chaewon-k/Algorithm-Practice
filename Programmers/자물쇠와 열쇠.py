def rotate(arr):
    rot_arr = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rot_arr[M-1-j][i] = arr[i][j]

    return rot_arr

def match(start_x, start_y, cnt, key, lock):
    global N, M
    key_x = key_y = 0
    # 각 비교 범위 (NxN 영역을 벗어나지 않게)
    if start_x + M >= N:
        end_x = N
    else:
        end_x = start_x + M

    if start_y + M >= N:
        end_y = N
    else:
        end_y = start_y + M

    # 홈에 돌기 맞추기
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            if lock[x][y] == 0 and key[key_x][key_y] == 1:
                cnt -= 1
            key_y += 1
        key_x += 1
        key_y = 0

    if cnt <= 0:
        return True
    else:
        return False

def solution(key, lock):
    zero_cnt = 0
    global M, N
    N, M = len(lock), len(key)


    # 자물쇠의 홈 개수 세기
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                zero_cnt += 1
    if zero_cnt == 0:
        return True

    # 90도 회전하기
    for t in range(4):
        # 각 시작점에서 비교
        for i in range(N):
            for j in range(N):
                if match(i, j, zero_cnt, key, lock) == True:
                    return True
        key = rotate(key)

    return False


print(solution([[1]], [[0]]))

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))