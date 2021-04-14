for t in range(1, int(input())+1):
    N, P = map(int, input().split())
    Q, R = N//P, N % P
    ans = (Q+1)**R * Q**(P-R)
    print(f'#{t} {ans}')