from collections import deque
def cut_nodes(g, cut, idx):
    queue = deque([idx])
    while queue:
        index = queue.popleft()
        cut[index] = 1
        for i in g[index]:
            queue.append(i)
    return cut

def dfs(g, depth_list, cutting, depth):
    global mini
    if depth == len(depth_list):
        cnt = len(g) - sum(cutting)
        if mini > cnt:
            mini = cnt
        return

    for select in depth_list[depth]:
        if cutting[select] == 0:
            cutting[select] = 1
            new_cutting = cut_nodes(g, cutting, select)
            dfs(g, depth_list, new_cutting, depth+1)
            cutting[select] = 0

    return mini

def solution(n, edges):
    global mini
    mini = n
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    depth_tree = [graph[0]]
    temp1 = graph[0][:]
    while True:
        temp2 = []
        for i in temp1:
            for j in graph[i]:
                temp2.append(j)
        temp1 = temp2
        depth_tree.append(temp1)

        if j == n-1:
            break

    return dfs(graph, depth_tree, [0]*(n+1), 0)

# print(solution(19,[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
print(solution(14,[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]))