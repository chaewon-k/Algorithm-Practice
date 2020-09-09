def find(v, row, num, result):
    v_twin = v[::1]
    if row == len(num):   result.append(v_twin)
    else:
        for i in num[row]:
            v_twin[row] = i
            find(v_twin, row+1, num, result)
    return result

def Compare(x, y):
    for m in range(len(x)):
        if x[m] == y[m] or y[m] == '*':
            continue
        else:   return False
    return True

def solution(user_id, banned_id):
    answer = 0
    num = [[] for _ in range(len(banned_id))]
    a = []
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            if len(user_id[i]) == len(banned_id[j]) and Compare(user_id[i], banned_id[j]) == True:
                num[j].append(i)
    result = []
    visited = [0] * len(user_id)
    result = find([0]*len(num), 0, num, result)
    set_result = []
    for i in result:
        temp = set(i)
        if temp not in set_result and len(temp) == len(banned_id):
            set_result.append(temp)
    answer = len(set_result)
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
resultt = solution(user_id, banned_id)
print(resultt)
