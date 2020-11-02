def qsort(Arr, l, h):
    if l < h:
        Arr, p = partition(Arr,l,h)
        qsort(Arr, 1, p-1)
        qsort(Arr, p+1, h)

def partition(Arr, l, h):
    pivot = Arr[l]
    i,j = l,h
    while i<=j:
        while Arr[i]<=pivot and i<h:
            i+=1
        while Arr[j]>=pivot and j>l:
            j-=1
        if i<j:
            Arr[i], Arr[j] = Arr[j], Arr[i]
    Arr[l], Arr[j] = Arr[j], Arr[l]
    return Arr,j

Arr = [3,4,5,2,8,1]
qsort(Arr, 0, 5)
print(Arr)



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