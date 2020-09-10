T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for node in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    for i in range(N-M, 0, -1):
        if i*2+1>N:
            tree[i] = tree[i*2]
        else:
            tree[i] = tree[i*2] + tree[i*2+1]
    print(f'#{t+1} {tree[L]}')