T =  int(input())

for t in range(1, T+1):
    N = float(input())
    result = ''
    flag = 0
    for i in range(1, 13):
        N *= 2
        result += str(int(N) % 2)
        if N % 1 == 0:
            flag = -1
            break

    if flag == -1:   print(f'#{t} {result}')
    else:
        print(f'#{t} overflow')

