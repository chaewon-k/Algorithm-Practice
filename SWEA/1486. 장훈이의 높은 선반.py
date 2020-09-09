def powerset(temp, n, k, cur_sum):
    global minimum
    if n == k:
        diff = cur_sum - B
        if diff >= 0 and minimum > diff:
            minimum = diff
            return
    else:
        temp[k] = 1
        powerset(temp, n, k+1, cur_sum+array[k])
        temp[k] = 0
        powerset(temp, n, k+1, cur_sum)

T = int(input())
for t in range(T):
    N, B = map(int,input().split())
    array = list(map(int, input().split()))
    temp = [0] * N; subset = []
    minimum = 100000000000

    powerset(temp, N, 0, 0)
    print(f'#{t+1} {minimum}')