T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))[::-1]
    maxi = arr[0]
    answer = 0
    result = [0]
    for i in range(1,N):
        if arr[i] < maxi:
            answer += maxi - arr[i]
        else:
            maxi = arr[i]
    print('#{} {}'.format(t+1, answer))

