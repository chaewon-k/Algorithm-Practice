def f1(N, M):   #바깥의 공기와 치즈 안의 빈공간을 dfs로 구분. (100x100이 최대니까 반복믄으로.)
    s = []
    s.append((0,0))
    v = [[0]*M for _ in range(N)]
    v[0][0] = 1
    while s:
        i,j = s.pop()
        for k in range(4):
            ni, nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj]==0 and v[ni][nj]==0:
                    s.append((ni,nj))
                    v[ni][nj] = 1
                elif arr[ni][nj]==1:    #공기칸 i,j 얖에 치즈인 경우
                    arr[ni][nj] = 0     #치즈 녹음

    #공기와 닿은 치즈 지우기
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] ==1:   # 치즈이고 인접된 공기가 있으면
                for r, c in ([(0,1),(0,-1),(1,0),(-1,0)]):
                    if v[i+r][j+c]==1:
                        arr[i][j] = 0
                    if arr[i][j]==1:
                        cnt += 1
    return cnt

di = [0,1,0,-1]
dj = [1,0,-1,0]
R, C = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
melt = 1
h = pre = 0
while True:
    cheeze = f1(R,C)  #공기칸 탐색
    pre = cheeze
    h += 1
print(h)