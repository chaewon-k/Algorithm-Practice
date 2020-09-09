T = int(input())

for t in range(T):
    N = int(input())
    a = int(input())
    arr = []

    for i in range(N):
        arr.append(a%10)
        a = a//10
    arr.reverse()

    cnt = 0
    result = 0
    i = 0

    while i < N:
        if arr[i] == 1:
            i+=1
            cnt += 1
            if cnt > result :
                result = cnt
        else:
            i += 1
            cnt = 0

    print(f'#{t+1} {result}')