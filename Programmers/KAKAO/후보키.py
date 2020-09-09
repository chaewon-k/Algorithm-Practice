def Minimal(ans_list, sub):
    if len(ans_list) == 0:
        return True
    else:
        for i in range(len(ans_list)):
            cnt = 0
            for j in range(len(ans_list[i])):
                if ans_list[i][j] in sub:
                    cnt += 1
            if cnt == len(ans_list[i]): return False
        return True

def Uniqeness(relation, sub):
    new_table = []
    for i in range(len(relation)):
        temp = []
        for j in range(len(sub)):
            temp.append(relation[i][sub[j]])
        new_table.append(temp)

    for i in new_table:
        if new_table.count(i) >= 2:    return False
    return True

def make_subarr(arr, sub_arr):
    for i in range(1 << len(arr)):
        temp = []
        for j in range(len(arr)):
            if i & (1 << j):    temp.append(arr[j])
        sub_arr.append(temp)
    return sub_arr

def solution(relation):
    answer = 0
    cnt = 0
    arr = []; sub_arr = []
    answer_list = []; result = []
    for i in range(len(relation[0])):
        arr.append(i)
    sub_arr = make_subarr(arr, sub_arr)
    for s in range(1, len(sub_arr)):
        if Uniqeness(relation, sub_arr[s]) == True:
            if Minimal(answer_list,sub_arr[s]) == True:
                answer_list.append(sub_arr[s])

    answer = len(answer_list)
    return answer


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
