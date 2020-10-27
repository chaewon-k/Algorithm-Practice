T = int(input())
for t in range(1, T+1):
    bit = input()

    print(f'#{t}', end=' ')
    for i in range(0,len(bit),7):
        result = 0
        temp = bit[i:i+7][::-1]
        for j in range(7):
            if temp[j] == '1':
                result += 2**(j)
        print(result,end=' ')
    print()
