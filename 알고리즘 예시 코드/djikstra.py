V, E = map(int, input().split())
INF = 10000000000
adj = [[INF]*V for _ in range(V)]
for i in range(E):  # 자기 자신인 경우
    adj[i][i] = 0

s = 0   # 시작 정점 번호
d = [x for x in adj[s]] # 출발로부터의 거리
u = [0]*V  # w로 선택 여부 (거리 확정)
cnt = 0
while cnt < V:      # 모든 노드가 w로 선택될 때까지
    cnt += 1
    w = 0
    minV = INF

    for i in range(V):  # u[w] == 0을 만족하고, d[w]가 최소인 w찾기 (알아서 구현해보기)
        if d[i] < minV and u[i] == 0:
            w = i
            minV = d[i]
    for v in range(V):
        if adj[w][v] != 0 and adj[w][v] != INF and u[v] == 0:   #인접이고, u에 포함되지 않은 경우
            d[v] = min(d[v], d[w]+adj[w][v])
