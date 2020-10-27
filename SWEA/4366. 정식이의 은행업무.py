T = int(input())
for t in range(1, T+1):
    bin = list(input())
    ter = list(input())

    flag = 0
    for i in range(len(bin)*2):
        temp_bin = bin[:]
        temp_bin[i // 2] = str(i % 2)
        a = ''.join(temp_bin)

        for j in range(len(ter)*3):
            temp_ter = ter[:]
            temp_ter[j // 3] = str(j % 3)
            b = ''.join(temp_ter)
            if int(a, 2) == int(b, 3):
                print(f'#{t} {int(a,2)}')
                flag = -1
                break
        if flag == -1:   break


