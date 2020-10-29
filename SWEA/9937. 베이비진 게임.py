def run_tri(arr):
    j = 0
    while j < 10:   # tri 판단
        if arr[j] == 3: return 1
        j += 1
    j = 0
    while j < 8:    # run 판단
        if arr[j] >= 1 and arr[j + 1] >= 1 and arr[j + 2] >= 1:   return 1
        j += 1

    return 0

T = int(input())
for t in range(1,T+1):
    card = list(map(int, input().split()))
    a = [0]*10
    b = [0]*10
    result = '0'

    for i in range(0,12,2):
        a[card[i]] += 1
        b[card[i+1]] += 1
        if i >= 2:
            if run_tri(a):
                result = '1'
                break
            if run_tri(b):
                result = '2'
                break
    print(f'#{t} {result}')