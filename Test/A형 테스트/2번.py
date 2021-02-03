T = int(input())
for test_case in range(1, T + 1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    bridge_list_1 = []  # 대각선
    bridge_list_2 = []  # 가로세로

    for i in range(W):
        if arr[0][i] == 0:
            j = 1
            while True:
                if i+1 >=W or j >= H:
                    break
                if arr[j][i+1] == 0:
                    if i+1 == W-1 or j == H-1:
                        bridge_list_1.append(i)
                        break
                else:
                    break
                j += 1

    print(bridge_list_1)

    #1,6,3,-1,91