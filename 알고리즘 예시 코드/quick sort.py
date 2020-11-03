def qsort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        qsort(A, l, p - 1)
        qsort(A, p + 1, r)

def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while A[i] <= p:
            i += 1
        while A[j] >= p:
            j -= 1
        if i < j:   A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

Arr = [3,4,5,2,8,1]
qsort(Arr, 0, 5)
print(Arr)
#
#
#
# def quicksort(A):
#     if len(A) <= 1:
#         return A
#     pivot = A[len(A)//2]
#     less, equal, bigger = [], [], []
#     for i in A:
#         if i<pivot: less.append(i)
#         elif i>pivot:   bigger.append(i)
#         else:   equal.append(i)
#     return quicksort(less)+equal+quicksort(bigger)
#
# print(quicksort([3,4,5,2,3,1]))