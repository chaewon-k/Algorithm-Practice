def dfs(begin, target, words, visited, cnt):
    global answer

    if cnt >= answer:
        return
    if begin == target:
        if answer > cnt:
            answer = cnt
        return cnt

    for i in range(len(words)):
        num = 0
        for j in range(len(begin)):
            if begin[j] != words[i][j]:
                num += 1
            if num > 1:
                break
        if num == 1 and not visited[i]:        # 단어 바꿀 수 있을 때
            visited[i] = 1
            dfs(words[i], target, words, visited, cnt+1)
            visited[i] = 0

    return cnt

def solution(begin, target, words):
    global answer
    answer = 100000000
    visited = [0] * len(words)
    if target not in words:
        return 0
    dfs(begin, target, words, visited, 0)

    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))