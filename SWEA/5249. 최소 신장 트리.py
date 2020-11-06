def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    if node_v > node_u:
        parent[node_v] = node_u
    else:
        parent[node_u] = node_v


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key=lambda a: a[2])
    parent = [i for i in range(V + 1)]
    result = cnt = 0

    while cnt < V:
        p, c, w = arr.pop(0)
        temp_p, temp_c = find(p), find(c)
        if temp_p != temp_c:
            union(temp_p, temp_c)
            result += w
            cnt += 1

    print(f'#{t} {result}')