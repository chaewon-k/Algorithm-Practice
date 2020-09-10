def inorder(i):
    global cnt
    if i > N:
        return
    else:
        inorder(i*2)
        tree[i] = cnt
        cnt += 1
        inorder(i*2+1)

T = int(input())
for t in range(T):
    N = int(input())
    cnt = 1
    tree = [0]*(N+1)
    inorder(1)
    print(f'#{t+1} {tree[1]} {tree[N//2]})