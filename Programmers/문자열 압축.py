def compare(splited, i):
    cnt = 1
    result = ""
    str1 = splited.pop(0)
    while splited:
        str2 = splited.pop(0)
        if str1 == str2:
           cnt += 1
        else:
            if cnt != 1:
                result += str(cnt)
            result += str1
            str1 = str2
            cnt = 1
    if cnt != 1:
        result += str(cnt)
    result += str1

    return len(result)

def solution(s):
    N = len(s)
    answer = N
    for i in range(1,N):
        splited = [s[j:j+i] for j in range(0,N,i)]
        temp_ans = compare(splited,i)
        if answer > temp_ans:
            answer = temp_ans

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))