def solution(priorities, location):
    answer = 0
    idx_list = [i for i in range(len(priorities))]
    while priorities:
        if len(priorities) == 1:
            return answer+1
        temp = priorities.pop(0)
        idx = idx_list.pop(0)
        if max(priorities) > temp:
            priorities.append(temp)
            idx_list.append(idx)
        else:
            answer += 1
            if idx == location: return answer
    return answer

# solution([2,1,3,2],2)
print(solution([9],0))