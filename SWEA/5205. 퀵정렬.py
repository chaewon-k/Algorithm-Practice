def quicksort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quicksort(A, l, p - 1)
        quicksort(A, p + 1, r)

def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:   A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

T = int(input())
for t in range(1, T+1):
    n = int(input())
    A = list(map(int, input().split()))
    quicksort(A,0,n-1)
    print(f'#{t} {A[n//2]}')