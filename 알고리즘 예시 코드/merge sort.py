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