from itertools import permutations
import math

def check(num):
    for j in range(2, int(math.sqrt(num))+1):       #수의 제곱근까지만 판별해도 ㄱㅊ (정수론)
        if num % j == 0:
            return False
    return True

def solution(numbers):
    answer = 0

    num_list = list(numbers)
    string = []
    for i in range(1, len(num_list)+1):
        permu = set(list(permutations(num_list, i)))
        for p in permu:
            temp = int("".join(p))
            if temp not in string:
                string.append(temp)
    for i in string:
        if i < 2:
            continue
        elif check(i):
            answer += 1

    return answer

print(solution("17"))