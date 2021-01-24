def ways(total, k):
    arr = [[0 for i in range(total+1)] for i in range(k + 1)]
    for i in range(1,total+1):
        arr[1][i] = 1
    for i in range(1, k+1):
        arr[i][0] = 1
    for i in range(2, k+1):
        for j in range(1, total+1):
            if j >= i:
                arr[i][j] = arr[i][j-i] + arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j]
    return arr[k][total]%1000000007

print(ways(842,91))