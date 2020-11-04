def Filtering(subset):
    new_set = []
    for w in range(len(subset)):
        if 'A' <= subset[w][0] <='Z' and 'A' <= subset[w][1] <='Z': new_set.append(subset[w])
    return new_set

def solution(str1, str2):
    answer = 0
    set1 = []
    set2 = []
    intersection = 0
    word1, word2 = str1.upper(), str2.upper()
    # 1. 부분 집합 만들기
    for i in range(len(word1) - 1):
        set1.append(word1[i:i + 2])
    for i in range(len(word2) - 1):
        set2.append(word2[i:i + 2])

    # 2. 각 부분 집합 필터링
    set1 = Filtering(set1)
    set2 = Filtering(set2)

    if len(set1) == 0 and len(set2) == 0:
        answer = 65536
        return answer

    print(set1)
    print(set2)

    # 3. 방문여부 리스트 생성 - 비트 마스킹
    visited = [0] * len(set2)

    # 4. 같은 원소 찾기
    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] == set2[j] and not visited[j]:
                visited[j] = 1
                break

    # 5. 계산
    intersection = visited.count(1)
    union = len(set1) + len(set2) - intersection
    answer = int(intersection * 65536 / union)

    return answer

answer = solution('FRANCE','french')

print(answer)