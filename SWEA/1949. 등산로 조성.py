def f(i, j, c, s, N, K):  # i j좌표, pre 이전 칸 높이, l 이전칸까지 등산로 길이, c 남은 깎음 횟수
    global maxV
    if maxV < s + 1:  # 등산로 길이 갱신
        maxV = s + 1

    v[i][j] = 1
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
            if arr[i][j] > arr[ni][nj]:
                f(ni, nj, c, s + 1, N, K)
            elif c > 0 and arr[i][j] > arr[ni][nj] - K:
                org = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                f(ni, nj, 0, s + 1, N, K)  # 필요한만큼만 현재칸을 깎음
                arr[ni][nj] = org
    v[i][j] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    # 등산로의 시작높이 찾기
    h = 0
    for i in range(N):
        for j in range(N):
            if h < arr[i][j]:
                h = arr[i][j]
    # h인 칸에서 시작
    maxV = 0  # 등산로 최장 길이
    for i in range(N):
        for j in range(N):
            if arr[i][j] == h:
                f(i, j, 1, 0, N, K)
    print(f'#{tc} {maxV}')