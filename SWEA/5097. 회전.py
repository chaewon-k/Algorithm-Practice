T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    li = list(map(int, input().split()))
    mod = M%N
    print(f'#{t+1} {li[mod]}')