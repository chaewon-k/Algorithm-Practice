T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    array = [input() for _ in range(n)]
    result = ""
    success = 0
    #가로
    for k in range(n):
        arr = array[k]
        rev_arr = arr[::-1]
        for i in range(n-m+1):
            sub_arr = arr[i:i+m]
            if sub_arr in rev_arr:
                result = "".join(sub_arr)
                success = 1
                break
        if success == 1:    break

    #세로
    for k in range(n):
        arr = ''
        for i in range(n):
            arr += array[i][k]

        rev_arr = arr[::-1]
        for i in range(n - m + 1):
            sub_arr = arr[i:i + m]
            if sub_arr in rev_arr:
                result = "".join(sub_arr)
                success = 1
                break
        if success == 1:    break

    print(f'#{t+1} {result}')