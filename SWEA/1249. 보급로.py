def f(N):
    q = [(0, 0)]
    d = [[10e5] * N for _ in range(N)]  # 각 칸의 복구 비용을 최대값으로 초기화
    d[0][0] = arr[0][0]  # 출발 칸의 복구 비용
    while q:  # 주변 칸의 비용을 확인할 칸이 남아 있을 때까지 순회
        i, j = q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:  # 유효한 칸이면
                if d[ni][nj] > d[i][j] + arr[ni][nj]:  # i, j에서 ni, nj로 들어가서 복구할 때의 비용이 더 작으면
                    d[ni][nj] = d[i][j] + arr[ni][nj]  # 비용 갱신
                    q.append((ni, nj))  # ni, nj 주변도 갱신 가능 --> 인큐
    return d[N - 1][N - 1]


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    r = f(N)
    print(f'#{t} {r}')