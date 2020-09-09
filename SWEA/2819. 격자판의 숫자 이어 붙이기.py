def dfs(s, e, path):
    path += str(arr[s][e])
    if len(path) == 7:
        result_set.append(path)
        return
    else:
        for d in range(4):
            tmp_s,tmp_e = s+dx[d], e+dy[d]
            if 0<= tmp_s < 4 and 0<= tmp_e < 4:
                dfs(tmp_s, tmp_e, path)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result_set = []
    path=''
    for i in range(4):
        for j in range(4):
            dfs(i, j, path)
    print(f'#{t+1} {len(set(result_set))}')