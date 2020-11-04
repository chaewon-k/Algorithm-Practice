def mst_prim(G, s):
    key = [INF] * N  # 가중치를 무한대로 초기화
    pi = [None] * N  # 트리에서 연결될 부모 정점 초기화
    visited = [False] * N  # 방문 여부 초기화
    key[s] = 0  # 시작 정점의 가중치를 0으로 설정

    for _ in range(N):  # 정점의 개수만큼 반복
        minIndex = -1
        min = INF
        for i in range(N):  # 방문 안한 정점 중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True  # 최소 가중치 정점 방문처리
        for v, val in G[minIndex]:  # 선택 정점의 인접한 정점에 대해서
            if not visited[v] and val < key[v]:
                key[v] = val  # 가중치 갱신
                pi[v] = minIndex  # 트리에서 연결될 부모 정점 갱신

