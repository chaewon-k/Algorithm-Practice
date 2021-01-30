import copy
def f(n, k, W, H, org):
    global minV
    if n == k:
        cnt = 0
        for i in range(H):  # 벽돌을 깨고 남은 벽돌 개수 확인
            for j in range(W):
                if org[i][j] != 0:
                    cnt += 1
        if minV > cnt:
            minV = cnt
    elif minV == 0:
        return
    else:
        for i in range(W):  # 중복순열
            dest = copy.deepcopy(org)   # 구슬을 쏘기 위한 복사본

            # i에 구슬 쏘기
            crack(i, N, W, H, dest)
            f(n + 1, k, W, H, dest)


def crack(c, N, W, H, br):
    q = []
    r = 0
    while (r < H and br[r][c] == 0):  # 맨 위 벽돌 찾기
        r += 1
    if r == H:  # 벽돌이 없는 경우
        return
    q.append((r, c))
    while q:
        i, j = q.pop(0)
        k = br[i][j]  # 벽돌의 제거 범위
        br[i][j] = 0
        for dis in range(1, k):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향
                ni = i + dis * di
                nj = j + dis * dj
                if 0 <= ni < H and 0 <= nj < W:
                    q.append((ni, nj))
    for k in range(W):  # 아래로 떨어뜨릴 벽돌 찾기
        st = []
        for j in range(H - 1, -1, -1):
            if br[j][k] != 0:  # 남은 벽돌을 순서대로 모으고
                st.append(br[j][k])
                br[j][k] = 0
        for j in range(0, len(st)):  # 벽돌더미에 복사
            br[H - 1 - j][k] = st[j]


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())  # N 구슬 개수, W 폭, H 높이
    org = [list(map(int, input().split())) for _ in range(H)]  # 벽돌 정보
    minV = 100000000  # 최소값 초기화
    f(0, N, W, H, org)  # 발사 위치를 정하고 구슬 발사
    print('#{} {}'.format(tc, minV))