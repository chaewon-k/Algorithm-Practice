def palin(array, maxi):
    for m in range(n, 0, -1):
        if maxi > m:
            return maxi
        for i in range(n-m+1):
            if m % 2 == 0:
                a = array[i:i+m//2]
                b = array[i+m//2:i+m][::-1]
            else:
                a = array[i:i + m // 2]
                b = array[i + m // 2 + 1:i + m][::-1]

            if a==b and maxi < m:
                maxi = m
    return maxi

n = 20
for T in range(1):
    t = int(input())
    array = [input() for _ in range(20)]
    result_max = 0
    # 가로
    for k in range(n):
        arr = array[k]
        result_max = palin(arr, result_max)

    # 세로
    for k in range(n):
        arr = ''
        for i in range(n):
            arr += array[i][k]
        result_max = palin(arr, result_max)

    print(f'#{T+1} {result_max}')