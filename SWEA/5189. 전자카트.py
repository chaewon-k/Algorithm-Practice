import itertools
def perm(start):
    global mini
    ssum = arr[0][start[0]]
    for j in range(len(start)-1):
        if ssum > mini:
            return
        ssum += arr[start[j]][start[j + 1]]
    ssum += arr[j+1][0]
    if ssum < mini:
        mini = ssum
    return

T = int(input())
for t in range(1,T+1):
    mini = 10000000
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(1,N)]
    idx_list = list(itertools.permutations(A))
    print(idx_list)

    for i in idx_list:
        perm(i)

    print(f'#{t} {mini}')