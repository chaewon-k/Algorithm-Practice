def solution(blocks):
    N = len(blocks)
    answer = [101]*(N*(N+1)//2)
    start_point = []    # 숫자의 위치에 따라 역순으로 시작할 수도 있음
    # 1. 피라미드 배열 세팅
    turn = 0
    for idx in range(len(blocks)):
        input_idx = turn + idx
        answer[input_idx+blocks[idx][0]] = blocks[idx][1]
        turn += idx

        if idx >= 2 and blocks[idx][0] >= (idx+1)//2:
            start_point.append(-1)
        else:
            start_point.append(1)
    print(start_point)

    # 2. 피라미드 채우기
    idx = 1
    row = 1
    while row < N:
        if start_point[row] == 1:   # (1) 순방향으로 탐색
            for i in range(idx, idx+row):
                temp = answer[i:i+2]    # 두 개씩 묶는다.
                # 각각 101일 경우 대체하기
                if temp[0] == 101:
                    answer[i] = answer[i - row] - answer[i + 1]
                else:
                    answer[i+1] = answer[i - row] - answer[i]

        else:                       # (2) 역방향으로 탐색
            for i in range(idx+row, idx, -1):
                temp = answer[i-1:i+1]
                if temp[0] == 101:
                    answer[i] = answer[i-(row+1)] - answer[i-1]
                else:
                    answer[i-1] = answer[i - (row + 1)] - answer[i]

        row += 1
        idx += row
        print(row,idx)
        print(answer)

    return answer

print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
# print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))