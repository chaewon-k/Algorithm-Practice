from heapq import heappop, heappush

def dijkstra(start,End):
    dist = [INF for _ in range(N+1)]
    dist[start] = 0        # 자신은 0
    queue = []             # priority queue
    heappush(queue, [0, start])
    while queue:
        min_dist = heappop(queue)   # 현재 위치로부터 가장 가까운 노드. min_dist = [거리,도착점]
        if min_dist[1] == End:
            break
        for end in graph[min_dist[1]]:
            if dist[end[0]] > min_dist[0] + end[1]:
                dist[end[0]] = min_dist[0] + end[1]
                heappush(queue, [dist[end[0]], end[0]])
    return dist

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    INF = 10 * E + 1
    for _ in range(E):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])

    print(f'#{t} {dijkstra(0,N)[N]}')