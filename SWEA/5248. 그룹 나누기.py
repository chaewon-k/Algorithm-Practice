# union set
def find_parent(temp):
    if tree[temp] != temp:
        tree[temp] = find_parent(tree[temp])
    return tree[temp]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:   tree[a] = b
    else: tree[b] = a

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [i for i in range(N+1)]
    for i in range(0, M):
        union(arr[2*i], arr[2*i+1])
    result = set()
    for i in tree:
        result.add(find_parent(i))
    print(f'#{t} {len(result)-1}')
