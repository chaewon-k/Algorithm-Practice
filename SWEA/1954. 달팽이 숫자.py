T = int(input())
for t in range(T):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    number = 1; row = 0; col = -1; flag = 1; cnt = N

    while 0 < cnt:
        for i in range(cnt):
            col += flag
            snail[row][col] = number
            number += 1
        cnt -= 1
        for i in range(cnt):
            row += flag
            snail[row][col] = number
            number += 1
        flag *= -1
    
    print(f'#{t+1}')
    for i in snail:
        for j in i:
            print(j , end=' ')
        print()