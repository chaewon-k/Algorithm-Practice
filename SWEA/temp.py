dir = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

for t in range(int(input())):
    N, M, K = map(int, input().split())
    arr = [[-1] * N for _ in range(N)]
    data_set = [list(map(int, input().split())) for _ in range(K)]

    idx = 0
    for r, c, num, d in data_set:
        arr[r][c] = idx
        idx += 1

    for _ in range(M):
        for data in data_set:
            if data[0] == -1:  # 이미 합쳐진 군집 (존재하지 않는 군집)
                continue

            index = arr[data[0]][data[1]]  # 인덱스 저장
            arr[data[0]][data[1]] = -1
            data[0] += dir[data[3]][0]  # 미생물 군집 이동
            data[1] += dir[data[3]][1]
            if data[0] == 0 or data[1] == 0:  # 1. 가장자리 도착했을 때
                data[2] //= 2  # 개체 수 반으로 줄이고
                if data[3] == 1 or data[3] == 3:  # 상하좌우를 각각 반대로 전환
                    data[3] += 1
                else:
                    data[3] -= 1
            if arr[data[0]][data[1]] != -1:  # 2. 이동하려는 칸에 이미 다른 군집이 있을 경우
                data_set[arr[data[0]][data[1]]][2] += data[2]  # 이미 있는 군집에 개수 합치고

                data[0] = data[1] = data[2] = data[3] = -1  # 초기화

            else:  # 3. 이동하려는 칸에 다른 군집이 없을 경우
                arr[data[0]][data[1]] = index
        print(data_set)

    print(sum(data_set[2]))

    # print(data_set)










