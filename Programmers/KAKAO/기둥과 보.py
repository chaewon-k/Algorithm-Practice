def build_or_remove(ans):
    for an in ans:
        x,y,a = an[0],an[1],an[2]
        if a == 0:          #기둥
            if y == 0 or [x, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x, y, 1] not in ans) or ([x - 1, y, 1] not in ans and [x, y, 1] in ans):
                continue
            else:
                return False
        else:               #보
            if y == 0:
                return False
            else:
                if ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans) or [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans:
                    continue
                else:
                    return False
    return True

def solution(n, build_frame):
    answer = []

    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 1:  #1. 설치
            answer.append([x,y,a])
            if build_or_remove(answer) == False:
                answer.remove([x,y,a])

        else:       #2. 제거
            answer.remove([x,y,a])
            if build_or_remove(answer) == False:
                answer.append([x,y,a])

    return sorted(answer)

print(solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
                       [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
                       [1, 1, 1, 0], [2, 2, 0, 1]]))