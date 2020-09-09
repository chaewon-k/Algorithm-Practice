T = int(input())
for t in range(T):
    p = input(); st = input()
    word_list = list(set(p))
    result = 0
    for i in word_list:
        cnt = 0
        for j in st:
            if i == j:  cnt += 1
        if result < cnt:    result = cnt
    print(f'#{t+1} {result}')
