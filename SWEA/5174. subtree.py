def inorder(node):
    global cnt
    if node:
        cnt += 1
        inorder(tree[node][0])
        inorder(tree[node][1])

T = int(input())
for t in range(T):
    E, N = map(int, input().split())
    cnt = 0
    temp = list(map(int, input().split()))
    V = max(temp)
    tree = [[0] * 3 for _ in range(V + 1)]

    for i in range(E):
        p, c = temp[i * 2], temp[i * 2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c  # left
        else:
            tree[p][1] = c  # right
        tree[c][2] = p  # parent
    inorder(N)
    print(f'#{t+1} {cnt}')