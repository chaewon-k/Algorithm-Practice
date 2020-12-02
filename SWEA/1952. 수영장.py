T = int(input())
for t in range(1, T+1):
    fare = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    memo = [0]*13   # dp

    for i in range(1,13):
        if i < 3:   # 1일, 한 달 이용권 비교
            memo[i] = memo[i-1] + min(schedule[i-1]*fare[0], fare[1])
        else:   # 1일, 한 달, 세 달 이용권 비교
            memo[i] = min(memo[i-1]+schedule[i-1]*fare[0], memo[i-1]+fare[1], memo[i-3]+fare[2])
    print(f'#{t} {min(memo[12], fare[3])}')


#### 교수님 풀이 ####
# T = int(input())
# for tc in range(1, T + 1):
#     day, month, quarter, year = map(int, input().split())  # 이용권 비용
#     table = [0] + list(map(int, input().split()))  # 월별 이용일
#
#     d = [0] * 13
#     for i in range(1, 13):
#         d[i] = d[i - 1] + min(table[i] * day, month)  # 1개월 단위 결제
#         if i >= 3:
#             d[i] = min(d[i], d[i - 3] + quarter)  # 1달 결제와 3개월 비교
#     print(f'#{tc} {min(year, d[12])}')