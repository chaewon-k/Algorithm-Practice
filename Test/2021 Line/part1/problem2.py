from re import compile
from collections import Counter

def solution(inp_str):
    answer = []
    arr = compile('[A-Za-z0-9~!@#$%^&*]+').findall(inp_str)

    if len(inp_str) < 8 or len(inp_str) > 15:   answer.append(1)
    if len(arr) == 0 or len(arr[0]) != len(inp_str):  answer.append(2)

    summ = 0
    if len(compile('[A-Z]').findall(inp_str)) > 0:  summ += 1
    if len(compile('[a-z]').findall(inp_str)) > 0:  summ += 1
    if len(compile('[0-9]').findall(inp_str)) > 0:    summ += 1
    if len(compile('[~!@#$%^&*]').findall(inp_str)) > 0:   summ += 1

    if summ < 3:    answer.append(3)

    count = end = 1
    string = inp_str[0]

    for i in range(1, len(inp_str)):
        while count < 4 and end < len(inp_str):
            if string == inp_str[i]:
                count += 1
            else:
                string = inp_str[i]
                break
            end += 1
        if count == 4:
            answer.append(4)
            break

    if max(Counter(inp_str).values()) >= 5: answer.append(5)

    if 0 < len(answer):
        return answer
    else:
        return [0]



print(solution("AaTa+!12-3"))
print(solution("aaaaZZZZ)"))
print(solution("CaCbCgCdC888834A"))
print(solution("UUUUU"))
print(solution("ZzZz9Z824"))
