def find(graph, node):
    queue = [node]
    parents = []
    while queue:
        parent = queue.pop(0)
        if (graph[parent]):
            queue.append(graph[parent][0])
        parents.append(parent)
    return parents

T = int(input())
for t in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        # 자식의 부모들을 추가
        graph[b].append(a)
    a, b = map(int, input().split())
    a_parents = find(graph, a)
    b_parents = find(graph, b)

    result = -1
    for i in range(len(a_parents)):
        for j in range(len(b_parents)):
            if a_parents[i] == b_parents[j]:
                result = a_parents[i]
                break
        if result != -1:
            break
    print(result)