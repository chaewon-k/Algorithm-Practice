T = int(input())
for t in range(T):
    N, question = map(int, input().split())
    score = [0]*(question)
    sol = list(map(int, input().split()))
    result = []
    for n in range(N):
        temp = list(map(int, input().split()))
        k = 1
        for i in range(question):
            if sol[i] == temp[i]:
                score[i] = k
                k += 1
            else:
                k = 1
        print(score)
        result.append(sum(score))
    print('#{} {}'.format(t+1, max(result)-min(result)))


