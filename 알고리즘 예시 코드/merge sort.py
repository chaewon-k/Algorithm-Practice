def divide(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list) // 2
    left = divide(unsorted_list[:mid])
    right = divide(unsorted_list[mid:])
    return merge(left, right)

def merge(left, right):
    left_len, right_len = len(left), len(right)
    left_idx = right_idx = 0
    sorted = []

    while left_idx < left_len and right_idx < right_len:
        if left[left_idx] <= right[right_idx]:
            sorted.append(left[left_idx])
            left_idx += 1
        else:
            sorted.append(right[right_idx])
            right_idx += 1

    if left_idx != left_len:
        while left_idx != left_len:
            sorted.append(left[left_idx])
            left_idx += 1

    if right_idx != right_len:
        while right_idx != right_len:
            sorted.append(right[right_idx])
            right_idx += 1

    return sorted


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = divide(arr)
    print(f'#{t} {arr}')


########### 더 빠른 merge sort ##############

def merge_sort(l):
    leng = len(l)
    if leng == 1:
        return l[:]
    center = leng // 2
    a = merge_sort(l[:center])
    b = merge_sort(l[center:])

    i = j = 0
    merg = []
    for _ in range(leng):
        if a[i] <= b[j]:
            merg.append(a[i])
            i += 1
            if i == leng // 2:
                merg += b[j:]
                break
        else:
            merg.append(b[j])
            j += 1
            if j == (leng + 1) // 2:
                merg += a[i:]
                break
    return merg


for tc in range(1, int(input()) + 1):
    N = int(input())
    l = list(map(int, input().split()))
    print(f'#{tc}', merge_sort(l)[N // 2])