bit = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    flag = 0
    key = ''

    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == '1':
                key = arr[i][j-55:j+1]
                flag = -1
                break
        if flag == -1:  break

    key_2 = []
    for i in range(0, len(key), 7):
        temp = key[i:i + 7]
        idx = bit[temp]
        key_2.append(idx)
    result = (key_2[0] + key_2[2] + key_2[4] + key_2[6]) * 3 + (key_2[1] + key_2[3] + key_2[5]) + key_2[7]

    if result % 10 == 0:
        print(f'#{t} {sum(key_2)}')
    else:
        print(f'#{t} 0')

