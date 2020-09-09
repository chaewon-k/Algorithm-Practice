T = int(input())

for t in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    summ = C[0]
    length = 1
    max_summ = max_length = result_len = 0 #차례대로 최고 합, 최고 길이, 부분집합 개수
    flag = 1 #아래 설명

    for i in range(N-1):
        if C[i] < C[i+1]:   #오름차순일 경우
            summ += C[i+1]
            length += 1
            if i == N-2:  #마지막 원소에 도착했을 경우 flag = -1로 설정하여 아래의 if문에 들어가도록 함 (max값과 비교하기 위해)
                flag = -1

        if C[i] > C[i+1] or flag == -1:     #내림차순이거나 마지막 원소에 도착했을 경우
            if max_length < length:         #1. 길이 비교
                max_summ = summ
                max_length = length

            if max_length == length:        #2. 총 합 크기 비교 (길이가 같을 경우)
                max_summ = max(max_summ, summ)
            
            if length >= 2:  # 길이가 2 이상일 때 부분집합의 개수 늘려줌.
                result_len += 1
            summ = C[i+1]   #초기화 
            length = 1

    if result_len == 0:
        max_summ = 0

    print(f'#{t+1} {result_len} {max_summ}')