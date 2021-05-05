# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    t, a, b = map(int, input().split())
    # union find
    if t == 0:
        union_parent(parent, a, b)
    
    # 두 원소가 같은 그룹인지 체크
    else:
        if find_parent(parent, parent[a]) == find_parent(parent, parent[b]):
            print("YES")
        else:
            print("NO")

# 3 3
# 0 2 3
# 0 1 2
# 1 1 3
# YES
# 0으로 시작하면 합치기, 1로 시작하면 같은 그룹인지 확인하기