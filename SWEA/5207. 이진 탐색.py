def bin_search(target, A):
    left = flag = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:    return True
        elif A[mid] > target:
            right = mid - 1
            if flag == 1:   return False
            flag = 1
        else:
            left = mid + 1
            if flag == -1:  return False
            flag = -1
    return False

T = int(input())
for t in range(1,T+1):
    N,M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        if bin_search(b, A) == True:
            cnt += 1
    print(f'#{t} {cnt}')


