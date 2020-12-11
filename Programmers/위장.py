def solution(clothes):
    answer = 1

    dic = {}
    for cloth in clothes:
        if cloth[1] not in dic: dic[cloth[1]] = {cloth[0]}
        else:   dic[cloth[1]].add(cloth[0])
    for key, value in dic.items():  answer *= len(value)+1

    return answer-1

# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     print(cnt)
#     print(cnt.keys())
#     print(cnt.values())
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"]]))