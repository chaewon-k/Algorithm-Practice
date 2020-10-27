T = int(input())
for t in range(1, T+1):
    N, hexa = map(str, input().split())
    new_N = int(N)
    bina = ''

    for i in hexa:
        bina += str(format(int(i,16), 'b').zfill(4))
    print(f'#{t} {bina}')