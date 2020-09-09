def bin_search(arr, key):
    cnt = 0
    start = 0; end = len(arr) - 1
    while start <= end:
        mid = int((start + end)/ 2)
        if arr[mid] == key: return cnt
        elif arr[mid] > key:    end = mid
        else:   start = mid
        cnt += 1
    return -1

T = int(input())
for t in range(T):
    P, A, B = map(int,input().split())
    book_list = []
    for i in range(P):
        book_list.append(i+1)
    cnt_a = bin_search(book_list, A); cnt_b = bin_search(book_list, B)

    if cnt_a < cnt_b:   winner = 'A'
    elif cnt_a > cnt_b: winner = 'B'
    else:   winner = '0'

    print(f'#{t+1} {winner}')