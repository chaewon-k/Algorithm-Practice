from itertools import combinations
from collections import defaultdict
# 딕셔너리의 기본 값을 정의하고 값이 없을 경우 에러를 출력하지 않고 기본값을 출력.
def solution(info, query):
    answer = []
    dic = defaultdict(list)  # 기본 값을 list로 지정
    for i in info:
        i = i.split()
        data = i[:-1]
        score = int(i[-1])

        for j in range(5):
            for c in combinations(data, j):     # 각 조합 구하기
                temp_key = ''.join(c)           # 각 조합 별로 문자열 합치기
                # print(temp_key)
                dic[temp_key].append(score)     # 딕셔너리에 추가

    for key in dic.keys():
        dic[key].sort()                         # 딕셔너리 각 요소 오름차순 정렬

    for q in query:                             # query도 위와 같이 분류
        q = q.split()
        q_score = int(q[-1])
        q = q[:-1]

        for i in range(3):                      # and와 - 제거하고 위와 같이 문자열로 합치기
            q.remove('and')
        while '-' in q:
            q.remove('-')
        temp_q = ''.join(q)

        # 이진탐색. 모든 점수를 비교하지 않고, 이미 오름차순 되어있는 배열에서 이진탐색으로 빠르게 서치.
        if temp_q in dic:
            scores = dic[temp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210",
                "python frontend senior chicken 150","cpp backend senior pizza 260",
                "java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))    #[1,1,1,1,2,4]