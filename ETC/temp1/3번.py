from copy import deepcopy
from collections import deque
def cut_nodes(g, cut, idx):
    queue = deque([idx])
    while queue:
        index = queue.popleft()
        cut[index] = 1
        for i in g[index]:
            queue.append(i)
    return cut


def dfs(g, cutting, start_idx, n):
    global mini
    if len(g[start_idx]) == 0:
        cnt = n - sum(cutting)
        if mini > cnt:
            mini = cnt
        return

    temps = g[start_idx]    # 특정 노드의 자식들
    for temp in temps:
        temp_cutting = cut_nodes(g, cutting, temp)     # 가지치기 처리
        
        for temp2 in temps:
            if temp2 != temp and temp_cutting[temp2] == 0:
                dfs(g, temp_cutting, temp2, n)


def solution(n, edges):
    global mini
    mini = n
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    print(graph)
    dfs(graph, [0]*(n+1), 0, n)
    return mini




print(solution(19,[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))