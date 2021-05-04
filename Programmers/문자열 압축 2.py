def compare(li):
    word = ''
    prev = li[0]
    cnt = 1
    for a in range(1, len(li)):
        if li[a] == prev:
            cnt += 1
        else:
            if cnt > 1:
                word += str(cnt)
            word += prev
            cnt = 1
            prev = li[a]

    if cnt > 1:
        word += str(cnt)
    word += prev

    return len(word)


def solution(s):
    answer = 1001
    for i in range(1, len(s) + 1):
        splited_list = []
        for j in range(0, len(s), i):
            splited_list.append(s[j:j + i])
        result = compare(splited_list)

        if answer > result:
            answer = result
    return answer