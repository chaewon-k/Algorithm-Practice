##백트래킹##
def cook(idx, sum_score, sum_calo):
    global ans
    if sum_calo > L:
        return

    if idx == N:
        if sum_score > ans:
            ans = sum_score
        return

    cook(idx+1, sum_score+score[idx], sum_calo+calo[idx])
    cook(idx+1, sum_score, sum_calo)


for t in range(1, int(input())):
    N, L = map(int, input().split())
    score, calo = [], []
    for _ in range(N):
        s,c = map(int, input().split())
        score.append(s)
        calo.append(c)

    ans = 0
    cook(0,0,0)
    print(f'{t} {ans}')
