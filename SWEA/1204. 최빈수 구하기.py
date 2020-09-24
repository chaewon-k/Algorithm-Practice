T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = -1
    result = 0
    sett = set(arr)
    sett2 = list(sett)
    sett2.sort()
    for i in sett2:
        cnt = arr.count(i)
        if cnt >= maxi:
            maxi = cnt
            result = i

    print('#{} {}'.format(n, result))
