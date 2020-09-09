def inorder(node):
    if node:
        inorder(tree[node][0])
        print(word[node],end='')
        inorder(tree[node][1])

for t in range(1, 11):
    N = int(input())
    arr = []
    word = [0]
    tree = [[0]*3 for _ in range(N+1)]
    for i in range(N):
        arr.append(input().split())
    for i in arr:
        word.append(i[1])
    for i in arr:
        if len(i) > 2:
            for j in range(2, len(i)):
                tree[int(i[0])][j-2] = int(i[j])
                tree[int(i[j])][2] = int(i[0])
    print(f'#{t}', end =' ')
    inorder(N)
    print()