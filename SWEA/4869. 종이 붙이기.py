T = int(input())
for t in range(T):
    N = int(input())
    f = [0] * 31
    f[1] = 1; f[2] = 3
    for i in range(3, 31):
        f[i] = f[i - 1] + 2 * f[i - 2]
    print(f'#{t+1} {f[N // 10]}')