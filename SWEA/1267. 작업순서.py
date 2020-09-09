## topological sorting ##

for t in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]    #인접 리스트
    connected = [0] * (V+1)             #부모 노드의 개수
    stack = []                          #부모 노드가 없는 vertex index 리스트
    result = []

    # 1. 인접 리스트 생성 (부모 노드의 개수를 함께 측정)
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
        connected[arr[i+1]] += 1

    # 2. 시작 노드 리스트
    for i in range(1, V+1):
        if connected[i] == 0:
            stack.append(i)

    # 3. main
    while stack:
        for i in range(len(stack)):
            temp = stack.pop(0)
            result.append(temp)
            for j in graph[temp]:
                connected[j] -= 1
                if connected[j] == 0:   stack.append(j)

    print(f'#{t}', end =' ')
    for i in result:
        print(i, end =' ')