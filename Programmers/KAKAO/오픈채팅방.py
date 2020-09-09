def solution(record):
    answer = []
    enter = {}
    for i in record:
        temp = i.split()
        if temp[0] != 'Leave':  enter[temp[1]] = temp[2]

    for i in record:
        temp = i.split()
        name = enter[temp[1]]
        if temp[0] == 'Enter':  answer.append(f'{name}님이 들어왔습니다.')
        elif temp[0] == 'Leave':    answer.append(f'{name}님이 나갔습니다.')
    return answer