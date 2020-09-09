#보이어-무어 알고리즘

T = int(input())
for t in range(T):
    p = input(); st = input()
    idx = i = len(p)-1
    result = 0

    while(i <= len(st)-1):
        if st[i] != p[idx]:
            move = 0
            for j in range(len(p)-1,-1,-1):
                if st[i] == p[j]:	break
                move += 1
            i += move

        else:
            temp = idx-1
            cnt = 1
            for j in range(i-1,i-len(p),-1):
                if st[j] == p[temp]:
                    cnt += 1
                    temp -= 1
                else:	break
            if cnt == len(p):
                result = 1
                break
            else:	i += cnt
    print(f'#{t+1} {result}')