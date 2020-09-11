def find_par(n):
    par = []
    temp = n
    while temp > 1:
        par.append(tree[temp][2])
        temp = tree[temp][2]
    return par

def counting(root):
    global cnt
    if root:
        left = counting(tree[root][0])
        right = counting(tree[root][1])
        return 1 + left + right
    return 0

T = int(input())
for t in range(T):
    V, E, a, b = map(int, input().split())
    tree = [[0]*3 for _ in range(V+1)]
    li = list(map(int, input().split()))

    for i in range(E):
        x = li[i*2]
        y = li[i*2+1]
        if tree[x][0] != 0: tree[x][1] = y
        else:   tree[x][0] = y
        tree[y][2] = x

    a_par = find_par(a)
    b_par = find_par(b)

    flag = result = 0
    for i in range(len(a_par)):
        for j in range(len(b_par)):
            if a_par[i] == b_par[j]:
                result = a_par[i]
                flag = -1
                break
        if flag == -1:  break

    print(f'#{t+1} {result} {counting(result)}')