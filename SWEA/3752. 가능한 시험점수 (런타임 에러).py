def make_subarr(arr, sub_arr):
    for i in range(1 << len(arr)):
        temp = 0
        for j in range(len(arr)):
            if i & (1 << j):    temp+=arr[j]
        if temp not in sub_arr:
            sub_arr.append(temp)
    return sub_arr

T = int(input())
for t in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    sub = []
    sub = make_subarr(scores, sub)
    print(f'#{t+1} {len(set(sub))}')

# 두번째 방법 (역시 런타임 에러..)
# import itertools
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     sum_list = []
#     for i in range(N+1):
#         subset = itertools.combinations(scores, i)
#         for sub in subset:
#             sum_list.append(sum(sub))
#     print(f'#{t+1} {len(set(sum_list))}')
