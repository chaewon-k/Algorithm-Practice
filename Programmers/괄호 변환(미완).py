def divide(p):
    start = end = 0
    for i in range(len(p)):
        if p[i] == '(': start += 1
        else:   end += 1
        if start == end:    return p[:i+1], p[i+1:]

def is_compare(u):
    cnt = 0
    if u[0] != '(':
        return False
    else:
        return True

def recursive(v):
    pass

def solution(p):
    answer = ''

    u, v = divide(p)

    if is_compare(u) == True:
        answer += u
    else:
        temp_answer = ''


    # print(answer)



    # recursive(p)

    return answer

# print("(()())()")
# print(")(")
print(solution("()))((()"))