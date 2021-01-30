dir = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]   # 상하좌우

for t in range(int(input())):
    N, M, K = map(int, input().split())
    data_set = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        idx = 0
        arr = [[-1] * N for _ in range(N)]
        for data in data_set:
            if data[0] == -1:  # 이미 합쳐진 군집 (존재하지 않는 군집)
                continue

            data[0] += dir[data[3]][0]  # 미생물 군집 이동
            data[1] += dir[data[3]][1]
            if data[0] == 0 or data[1] == 0 or data[0] == N-1 or data[1] == N-1:  # 1. 가장자리 도착했을 때
                data[2] //= 2  # 개체 수 반으로 줄이고
                if data[3] == 1 or data[3] == 3:  # 상하좌우를 각각 반대로 전환
                    data[3] += 1
                else:
                    data[3] -= 1
            past_idx = arr[data[0]][data[1]]
            if past_idx == -1:     # 2. 이동하려는 칸에 다른 군집이 없을 경우
                arr[data[0]][data[1]] = idx     # 이동한 위치 표시

            else:       # 3. 이동하려는 칸에 다른 군집이 있을 경우
                if data[2] > data_set[past_idx][2]:
                    data[2] += data_set[past_idx][2]
                    data_set[past_idx][0] = -1
                    arr[data[0]][data[1]] = idx
                else:
                    data_set[past_idx][2] += data[2]
                    data[0] = -1
            idx += 1
    result = 0
    for data in data_set:
        if data[0] != -1:
            result += data[2]
    print('#{} {}'.format(t+1, result))

