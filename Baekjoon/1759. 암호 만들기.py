from itertools import combinations

L, C = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
group = ['a','e','i','o','u']

combi = combinations(alpha,L)

for c in combi:
    cnt1 = cnt2 = 0
    for i in c:
        if i in group:  cnt1 += 1
        else:   cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        print(''.join(c))

