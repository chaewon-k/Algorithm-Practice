N = int(input())
maxi = -1
for i in range(N+1):
    result = [N,i]

    while True:
        n = len(result)
        temp = result[n-2]-result[n-1]
        if temp < 0:
            break
        else:
            result.append(temp)
    if maxi < len(result):
        maxi = len(result)
        final = result[:]

print(maxi)
for i in final:
    print(i, end=' ')


